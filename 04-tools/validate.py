#!/usr/bin/env python3
"""
CatWeb JSON Validator & Object Counter (Python version)

Usage:
  python validate.py path/to/site.json
  python validate.py path/to/folder/
  python validate.py site.json --strict
"""

import json
import sys
import re
from pathlib import Path
from collections import defaultdict

FORBIDDEN_KEYS = {
    "layout_order", "cell_size", "padding", "margin", "gap",
    "border-radius", "borderRadius", "flex", "justifyContent"
}
VALID_GLOBALID = re.compile(r"^[A-Za-z0-9]{2,3}$")
CONTROL_IDS = {"18","19","20","21","22","23","25","112","125","126","37","38","92","93","44","45","46","47"}

def walk(node, stats, path="root"):
    if not isinstance(node, (dict, list)):
        return
    if isinstance(node, list):
        for i, child in enumerate(node):
            walk(child, stats, f"{path}[{i}]")
        return

    cls = node.get("class")
    if cls:
        stats["elements"] += 1
        stats["by_class"][cls] += 1

        gid = node.get("globalid")
        if gid:
            if not VALID_GLOBALID.match(gid):
                stats["errors"].append(f'Invalid globalid "{gid}" at {path}')
            if gid in stats["globalids"]:
                stats["errors"].append(f'Duplicate globalid "{gid}" at {path}')
            stats["globalids"].add(gid)

        alias = node.get("alias")
        if alias:
            if alias in stats["aliases"]:
                stats["errors"].append(f'Duplicate alias "{alias}" at {path}')
            stats["aliases"].add(alias)

        for k, v in node.items():
            if k in FORBIDDEN_KEYS:
                stats["errors"].append(f'Forbidden key "{k}" at {path}')
            if v is not None and not isinstance(v, (dict, list, str)):
                stats["errors"].append(f'Non-string scalar "{k}": {type(v).__name__} at {path}')

        if cls == "script":
            stats["scripts"] += 1
            content = node.get("content")
            if not isinstance(content, list):
                stats["errors"].append(f"script.content must be array at {path}")
            else:
                for i, block in enumerate(content):
                    if "id" not in block:
                        stats["errors"].append(f"Script block missing id at {path}.content[{i}]")
                    if "actions" in block and not isinstance(block["actions"], list):
                        stats["errors"].append(f"actions must be array at {path}.content[{i}]")
                    if str(block.get("id")) in CONTROL_IDS and "actions" in block:
                        stats["errors"].append(
                            f'Control-flow id {block["id"]} has nested "actions" at {path}.content[{i}]'
                        )

    if "children" in node:
        walk(node["children"], stats, f"{path}.children")

def validate_file(path: Path, strict=False):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {"file": str(path), "ok": False, "errors": [f"JSON parse error: {e}"], "stats": None}

    stats = {
        "elements": 0,
        "scripts": 0,
        "by_class": defaultdict(int),
        "globalids": set(),
        "aliases": set(),
        "errors": [],
        "warnings": [],
    }

    if not isinstance(data, dict):
        stats["errors"].append("Root must be a JSON object")
    else:
        if "favicon" not in data:
            stats["warnings"].append("Missing favicon")
        if "title" not in data:
            stats["warnings"].append("Missing title")
        if "background" not in data:
            stats["warnings"].append("Missing background")
        wc = data.get("webcontent")
        if wc is None:
            stats["errors"].append("Missing webcontent")
        elif not isinstance(wc, list):
            stats["errors"].append("webcontent must be an array")
        else:
            walk(wc, stats, "webcontent")

    ok = len(stats["errors"]) == 0 and (not strict or len(stats["warnings"]) == 0)
    return {"file": str(path), "ok": ok, "errors": stats["errors"], "warnings": stats["warnings"], "stats": stats}

def collect_files(target: Path):
    if target.is_file():
        return [target]
    return list(target.rglob("*.json"))

def main():
    args = sys.argv[1:]
    if not args:
        print("Usage: python validate.py <file-or-folder> [--strict]")
        sys.exit(1)

    strict = "--strict" in args
    target = Path(next(a for a in args if not a.startswith("--")))
    files = collect_files(target)

    total_errors = 0
    for f in files:
        r = validate_file(f, strict)
        print(f"\n=== {r['file']} ===")
        if r["stats"]:
            s = r["stats"]
            print(f"Elements: {s['elements']}  |  Scripts: {s['scripts']}")
            by = ", ".join(f"{k}:{v}" for k, v in sorted(s["by_class"].items())) or "(none)"
            print("By class:", by)
        if r["errors"]:
            print("ERRORS:")
            for e in r["errors"]:
                print("  ✗", e)
            total_errors += len(r["errors"])
        if r["warnings"]:
            print("WARNINGS:")
            for w in r["warnings"]:
                print("  ⚠", w)
        if r["ok"]:
            print("✓ OK")

    sys.exit(1 if total_errors else 0)

if __name__ == "__main__":
    main()
