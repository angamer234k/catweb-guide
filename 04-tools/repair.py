#!/usr/bin/env python3
"""
CatWeb JSON Repair (conservative)

Only applies fixes when the site JSON is structurally broken or uses
known-invalid keys/types. If the schema already looks fine, prints
NO_REPAIR_NEEDED and exits 0 without changing the file.

Usage:
  python repair.py path/to/site.json
  python repair.py path/to/site.json --write   # write repaired JSON next to input
  python repair.py path/to/site.json --stdout  # print repaired JSON only
  cat site.json | python repair.py -          # read stdin

Exit codes:
  0 — already fine (no changes) OR successfully repaired
  1 — parse failure / unrecoverable
"""

from __future__ import annotations

import json
import sys
import re
import copy
from pathlib import Path

FORBIDDEN_KEY_MAP = {
    "layout_order": "order",
    "cell_size": "size",
}

DROP_KEYS = {
    "margin", "gap", "border-radius", "borderRadius",
    "flex", "justifyContent", "justify_content", "alignItems", "align_items",
}

VALID_GLOBALID = re.compile(r"^[A-Za-z0-9]{2,3}$")
CONTROL_IDS = {
    "18", "19", "20", "21", "22", "23", "25", "112",
    "125", "126", "37", "38", "92", "93", "44", "45", "46", "47",
}


def _stringify_scalars(obj, changes: list, path: str = "root"):
    if isinstance(obj, dict):
        for k, v in list(obj.items()):
            p = f"{path}.{k}"
            if isinstance(v, (dict, list)):
                _stringify_scalars(v, changes, p)
            elif v is None or isinstance(v, bool) or isinstance(v, (int, float)):
                obj[k] = "true" if v is True else "false" if v is False else "null" if v is None else str(v)
                changes.append(f"stringified scalar {p}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            p = f"{path}[{i}]"
            if isinstance(v, (dict, list)):
                _stringify_scalars(v, changes, p)
            elif v is None or isinstance(v, bool) or isinstance(v, (int, float)):
                obj[i] = "true" if v is True else "false" if v is False else "null" if v is None else str(v)
                changes.append(f"stringified scalar {p}")


def _fix_keys(obj, changes: list, path: str = "root"):
    if isinstance(obj, dict):
        for k in list(obj.keys()):
            p = f"{path}.{k}"
            if k in FORBIDDEN_KEY_MAP:
                new_k = FORBIDDEN_KEY_MAP[k]
                if new_k not in obj:
                    obj[new_k] = obj.pop(k)
                    changes.append(f'renamed "{k}" → "{new_k}" at {p}')
                else:
                    del obj[k]
                    changes.append(f'dropped duplicate forbidden key "{k}" at {p}')
            elif k in DROP_KEYS:
                del obj[k]
                changes.append(f'dropped invalid key "{k}" at {p}')
            else:
                _fix_keys(obj[k], changes, p)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            _fix_keys(v, changes, f"{path}[{i}]")


def _fix_script_control_flow(node, changes: list, path: str = "root"):
    if not isinstance(node, dict):
        if isinstance(node, list):
            for i, c in enumerate(node):
                _fix_script_control_flow(c, changes, f"{path}[{i}]")
        return

    if node.get("class") == "script":
        content = node.get("content")
        if isinstance(content, list):
            for i, block in enumerate(content):
                if not isinstance(block, dict):
                    continue
                bp = f"{path}.content[{i}]"
                bid = str(block.get("id", ""))
                if bid in CONTROL_IDS and "actions" in block:
                    nested = block.pop("actions")
                    changes.append(f"flattened nested actions on control-flow id {bid} at {bp}")
                    if isinstance(nested, list):
                        for j, a in enumerate(nested):
                            content.insert(i + 1 + j, a)
                if "actions" in block and isinstance(block["actions"], list):
                    for j, a in enumerate(block["actions"]):
                        _fix_script_control_flow(a, changes, f"{bp}.actions[{j}]")

    if "children" in node and isinstance(node["children"], list):
        for i, c in enumerate(node["children"]):
            _fix_script_control_flow(c, changes, f"{path}.children[{i}]")


def _ensure_root_shape(data, changes: list):
    if not isinstance(data, dict):
        changes.append("root was not an object — cannot auto-wrap safely")
        return data

    if "webcontent" not in data:
        if "class" in data:
            el = {k: v for k, v in data.items() if k not in ("favicon", "title", "background", "thumbnail_id", "thumbnail")}
            meta = {k: data[k] for k in ("favicon", "title", "background", "thumbnail_id", "thumbnail") if k in data}
            data = {
                "favicon": meta.get("favicon", "128490289676597"),
                "title": meta.get("title", "Untitled"),
                "background": meta.get("background", "#ffffff"),
                "webcontent": [el],
            }
            changes.append("wrapped single element into top-level site object with webcontent")
        else:
            changes.append("missing webcontent — cannot invent tree")
    elif not isinstance(data["webcontent"], list):
        data["webcontent"] = [data["webcontent"]]
        changes.append("wrapped webcontent into array")

    for key, default in (("favicon", "128490289676597"), ("title", "Untitled"), ("background", "#ffffff")):
        if key not in data:
            data[key] = default
            changes.append(f'added missing top-level "{key}"')
        elif not isinstance(data[key], str):
            data[key] = str(data[key])
            changes.append(f'stringified top-level "{key}"')

    return data


def _fix_globalids(data, changes: list):
    used = set()
    counter = [0]
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    def next_gid():
        while True:
            n = counter[0]
            counter[0] += 1
            if n < 62 * 62:
                a, b = divmod(n, 62)
                gid = alphabet[a % 62] + alphabet[b]
            else:
                n2 = n - 62 * 62
                a, r = divmod(n2, 62 * 62)
                b, c = divmod(r, 62)
                gid = alphabet[a % 62] + alphabet[b] + alphabet[c]
            if gid not in used:
                return gid

    def walk(node, path):
        if isinstance(node, list):
            for i, c in enumerate(node):
                walk(c, f"{path}[{i}]")
            return
        if not isinstance(node, dict):
            return
        if node.get("class"):
            gid = node.get("globalid")
            if not gid or not isinstance(gid, str) or not VALID_GLOBALID.match(gid) or gid in used:
                new_gid = next_gid()
                node["globalid"] = new_gid
                changes.append(f'assigned globalid "{new_gid}" at {path}')
                used.add(new_gid)
            else:
                used.add(gid)
        if "children" in node:
            walk(node["children"], f"{path}.children")
        if node.get("class") == "script" and isinstance(node.get("content"), list):
            for i, block in enumerate(node["content"]):
                if isinstance(block, dict):
                    bg = block.get("globalid")
                    if block.get("id") is not None:
                        if not bg or not isinstance(bg, str) or not VALID_GLOBALID.match(str(bg)) or bg in used:
                            new_gid = next_gid()
                            block["globalid"] = new_gid
                            changes.append(f'assigned globalid "{new_gid}" at {path}.content[{i}]')
                            used.add(new_gid)
                        else:
                            used.add(bg)
                    if isinstance(block.get("actions"), list):
                        for j, act in enumerate(block["actions"]):
                            if isinstance(act, dict):
                                ag = act.get("globalid")
                                if not ag or not isinstance(ag, str) or not VALID_GLOBALID.match(str(ag)) or ag in used:
                                    new_gid = next_gid()
                                    act["globalid"] = new_gid
                                    changes.append(f'assigned globalid "{new_gid}" at {path}.content[{i}].actions[{j}]')
                                    used.add(new_gid)
                                else:
                                    used.add(ag)

    if isinstance(data, dict) and "webcontent" in data:
        walk(data["webcontent"], "webcontent")


def needs_repair(data) -> list:
    issues = []
    if not isinstance(data, dict):
        issues.append("root_not_object")
        return issues
    if "webcontent" not in data:
        issues.append("missing_webcontent")
    elif not isinstance(data.get("webcontent"), list):
        issues.append("webcontent_not_array")

    def scan(node, path="root"):
        if isinstance(node, list):
            for i, c in enumerate(node):
                scan(c, f"{path}[{i}]")
            return
        if not isinstance(node, dict):
            return
        for k, v in node.items():
            if k in FORBIDDEN_KEY_MAP or k in DROP_KEYS:
                issues.append(f"bad_key:{k}@{path}")
            if v is not None and not isinstance(v, (dict, list, str)):
                issues.append(f"non_string:{k}@{path}")
        if node.get("class") == "script":
            content = node.get("content")
            if isinstance(content, list):
                for i, block in enumerate(content):
                    if isinstance(block, dict):
                        bid = str(block.get("id", ""))
                        if bid in CONTROL_IDS and "actions" in block:
                            issues.append(f"nested_actions@{path}.content[{i}]")
        if "children" in node:
            scan(node["children"], f"{path}.children")
        if node.get("class") and "globalid" in node:
            gid = node.get("globalid")
            if not isinstance(gid, str) or not VALID_GLOBALID.match(gid):
                issues.append(f"bad_globalid@{path}")

    if isinstance(data, dict) and isinstance(data.get("webcontent"), list):
        scan(data["webcontent"], "webcontent")
    return issues


def repair(data):
    changes = []
    data = copy.deepcopy(data)
    data = _ensure_root_shape(data, changes)
    _fix_keys(data, changes)
    _stringify_scalars(data, changes)
    if isinstance(data, dict) and isinstance(data.get("webcontent"), list):
        for i, el in enumerate(data["webcontent"]):
            _fix_script_control_flow(el, changes, f"webcontent[{i}]")
    _fix_globalids(data, changes)
    return data, changes


def main():
    args = sys.argv[1:]
    write = "--write" in args
    stdout_only = "--stdout" in args
    args = [a for a in args if not a.startswith("--")]

    if not args:
        print("Usage: python repair.py <file.json|- > [--write] [--stdout]", file=sys.stderr)
        sys.exit(1)

    target = args[0]
    if target == "-":
        raw = sys.stdin.read()
        path = None
    else:
        path = Path(target)
        raw = path.read_text(encoding="utf-8")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"PARSE_ERROR: {e}", file=sys.stderr)
        sys.exit(1)

    issues = needs_repair(data)
    if not issues:
        print("NO_REPAIR_NEEDED")
        print("Schema looks fine — no automatic changes applied.")
        if stdout_only:
            print(json.dumps(data, indent=2, ensure_ascii=False))
        sys.exit(0)

    repaired, changes = repair(data)
    print(f"REPAIRED ({len(changes)} change(s))")
    for c in changes:
        print(f"  • {c}")

    out = json.dumps(repaired, indent=2, ensure_ascii=False)
    if stdout_only:
        print(out)
    elif write and path:
        out_path = path.with_suffix(".repaired.json")
        out_path.write_text(out + "\n", encoding="utf-8")
        print(f"Wrote {out_path}")
    else:
        print("--- repaired JSON ---")
        print(out)

    sys.exit(0)


if __name__ == "__main__":
    main()
