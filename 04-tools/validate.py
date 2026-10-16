#!/usr/bin/env python3
"""
CatWeb JSON Validator & Object Counter

Catches the failures that import but hang publish / break runtime:
  - Wrong action `text` slot counts (SiteGPT shapes)
  - Values stuffed into labels ("Split (x)" style)
  - globalid charset / length on elements AND script actions
  - Object refs that look like aliases
  - Filter-risk words (warning)
  - Forbidden keys, non-string scalars, nested control-flow actions

Usage:
  python validate.py path/to/site.json
  python validate.py path/to/folder/
  python validate.py site.json --strict
"""

from __future__ import annotations

import json
import sys
import re
from pathlib import Path
from collections import defaultdict

# id -> (expected text length, human name)
# Source: SiteGPT V11 §5.5 + v2.19 addendum. One source of truth for counts.
import sys
from pathlib import Path as _Path
sys.path.insert(0, str(_Path(__file__).resolve().parent))
from action_shapes import ACTION_SHAPES

EVENT_IDS = {"0", "1", "2", "3", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"}
CONTROL_IDS = {
    "18", "19", "20", "21", "22", "23", "25", "112",
    "125", "126", "37", "38", "92", "93", "44", "45", "46", "47",
}

FORBIDDEN_KEYS = {
    "layout_order", "cell_size", "margin", "gap",
    "border-radius", "borderRadius", "flex", "justifyContent",
    "justify_content", "alignItems", "align_items",
}
# padding is valid on UIListLayout / UIGridLayout — not forbidden

VALID_GLOBALID = re.compile(r"^[A-Za-z0-9]{2,3}$")
# Labels that look like values were stuffed in: "Split (foo)", "Set (x) text to"
STUFFED_LABEL = re.compile(r"^.+\([^)]*\)\s*$")
FILTER_WORDS = {
    "paste", "clipboard", "http://", "https://", "discord.gg",
}

TOP_LEVEL_ALLOWED = {
    "favicon", "title", "background", "webcontent",
    "thumbnail_id", "thumbnail",
}


def is_param_obj(x) -> bool:
    return isinstance(x, dict) and ("t" in x or "value" in x)


def check_action_text(aid: str, text, path: str, errors: list, warnings: list):
    if not isinstance(text, list):
        errors.append(f"INVALID_ACTION_TEXT id={aid} at {path}: text must be array")
        return

    # Note: labels like "Set (bd)" with () are the official annotation convention
    # (SiteGPT §5.1a) — do NOT flag them. Wrong shapes are caught by slot count.

    if aid not in ACTION_SHAPES:
        if aid not in EVENT_IDS:
            warnings.append(f"UNKNOWN_ACTION_ID id={aid} at {path} (not in SiteGPT table)")
        return

    expected_n, name = ACTION_SHAPES[aid]
    got_n = len(text)
    if got_n != expected_n:
        errors.append(
            f"INVALID_ACTION_ARGS id={aid} ({name}) at {path}: "
            f"expected {expected_n} slots, got {got_n}"
        )
        return

    # Type checks: alternating isn't universal — check object vs string roughly
    # For each slot: if expected is fixed length, param objects should have t/value
    for i, slot in enumerate(text):
        if isinstance(slot, dict):
            if "t" not in slot and "value" not in slot:
                warnings.append(
                    f"PARAM_SHAPE id={aid} at {path}.text[{i}]: object missing t/value keys"
                )
        elif not isinstance(slot, str):
            errors.append(
                f"INVALID_ACTION_ARGS id={aid} at {path}.text[{i}]: "
                f"slot must be string or param object, got {type(slot).__name__}"
            )


def check_filter_words(obj, path: str, warnings: list):
    if isinstance(obj, str):
        low = obj.lower()
        for w in FILTER_WORDS:
            if w in low:
                warnings.append(f'FILTER_WORD at {path}: contains "{w}" (may become #######)')
                break
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if k in ("text", "tooltip", "title", "placeholder", "alias"):
                check_filter_words(v, f"{path}.{k}", warnings)
            elif k == "value" and isinstance(v, str):
                check_filter_words(v, f"{path}.value", warnings)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            if isinstance(v, str):
                check_filter_words(v, f"{path}[{i}]", warnings)


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
        if gid is not None:
            if not isinstance(gid, str) or not VALID_GLOBALID.match(gid):
                stats["errors"].append(
                    f'Invalid globalid "{gid}" at {path} (need [A-Za-z0-9]{{2,3}})'
                )
            elif gid in stats["globalids"]:
                stats["errors"].append(f'Duplicate globalid "{gid}" at {path}')
            else:
                stats["globalids"].add(gid)
        else:
            stats["errors"].append(f"Missing globalid at {path} (class={cls})")

        alias = node.get("alias")
        if alias:
            if alias in stats["aliases"]:
                stats["errors"].append(f'Duplicate alias "{alias}" at {path}')
            stats["aliases"].add(alias)
            stats["alias_to_path"][alias] = path

        for k, v in node.items():
            if k in FORBIDDEN_KEYS:
                stats["errors"].append(f'Forbidden key "{k}" at {path}')
            if v is not None and not isinstance(v, (dict, list, str)):
                stats["errors"].append(
                    f'Non-string scalar "{k}": {type(v).__name__} at {path}'
                )

        # Filter words on display fields
        for fk in ("text", "tooltip", "placeholder", "title"):
            if fk in node:
                check_filter_words(node[fk], f"{path}.{fk}", stats["warnings"])

        if cls == "script":
            stats["scripts"] += 1
            content = node.get("content")
            if not isinstance(content, list):
                stats["errors"].append(f"script.content must be array at {path}")
            else:
                for i, block in enumerate(content):
                    bp = f"{path}.content[{i}]"
                    if not isinstance(block, dict):
                        stats["errors"].append(f"Script block must be object at {bp}")
                        continue
                    if "id" not in block:
                        stats["errors"].append(f"Script block missing id at {bp}")
                    bid = str(block.get("id", ""))

                    # globalid on every block
                    bg = block.get("globalid")
                    if bg is not None:
                        if not isinstance(bg, str) or not VALID_GLOBALID.match(bg):
                            stats["errors"].append(
                                f'Invalid globalid "{bg}" at {bp} (need [A-Za-z0-9]{{2,3}})'
                            )
                        elif bg in stats["globalids"]:
                            stats["errors"].append(f'Duplicate globalid "{bg}" at {bp}')
                        else:
                            stats["globalids"].add(bg)
                    else:
                        stats["warnings"].append(f"Missing globalid on script block at {bp}")

                    # Control-flow must not nest actions
                    if bid in CONTROL_IDS and "actions" in block:
                        stats["errors"].append(
                            f'Control-flow id {bid} has nested "actions" at {bp}'
                        )

                    # Event / define-function at top of content may have actions
                    if "actions" in block:
                        if not isinstance(block["actions"], list):
                            stats["errors"].append(f"actions must be array at {bp}")
                        else:
                            for j, act in enumerate(block["actions"]):
                                ap = f"{bp}.actions[{j}]"
                                if not isinstance(act, dict):
                                    stats["errors"].append(f"Action must be object at {ap}")
                                    continue
                                aid = str(act.get("id", ""))
                                ag = act.get("globalid")
                                if ag is not None:
                                    if not isinstance(ag, str) or not VALID_GLOBALID.match(ag):
                                        stats["errors"].append(
                                            f'Invalid globalid "{ag}" at {ap} '
                                            f"(need [A-Za-z0-9]{{2,3}})"
                                        )
                                    elif ag in stats["globalids"]:
                                        stats["errors"].append(
                                            f'Duplicate globalid "{ag}" at {ap}'
                                        )
                                    else:
                                        stats["globalids"].add(ag)
                                else:
                                    stats["warnings"].append(
                                        f"Missing globalid on action at {ap}"
                                    )

                                check_action_text(
                                    aid, act.get("text"), ap,
                                    stats["errors"], stats["warnings"],
                                )
                                # Object-ref lint
                                lint_object_refs(act.get("text"), ap, stats)

                    # Event / Define-function text: only verify known event ids
                    # (do NOT apply ACTION_SHAPES — ids overlap, e.g. event 0 vs action 0)
                    if bid and bid not in EVENT_IDS and "actions" in block:
                        # Top-level content entry that isn't a known event
                        stats["warnings"].append(
                            f"UNKNOWN_EVENT_ID id={bid} at {bp}"
                        )

    if "children" in node:
        walk(node["children"], stats, f"{path}.children")


def lint_object_refs(text, path, stats):
    if not isinstance(text, list):
        return
    known = stats["globalids"]
    aliases = stats["aliases"]
    for i, slot in enumerate(text):
        if not isinstance(slot, dict):
            continue
        if slot.get("t") != "object":
            continue
        val = slot.get("value")
        if not isinstance(val, str) or not val:
            continue
        # If it looks like an alias (longer / has underscore) and isn't a known globalid
        if val not in known:
            if val in aliases or len(val) > 3 or "_" in val or not VALID_GLOBALID.match(val):
                stats["warnings"].append(
                    f'OBJECT_REF at {path}.text[{i}]: value "{val}" is not a known globalid '
                    f"(scripts resolve by globalid, not alias)"
                )


def validate_data(data, strict=False):
    stats = {
        "elements": 0,
        "scripts": 0,
        "by_class": defaultdict(int),
        "globalids": set(),
        "aliases": set(),
        "alias_to_path": {},
        "errors": [],
        "warnings": [],
    }

    if not isinstance(data, dict):
        stats["errors"].append("Root must be a JSON object")
        return stats

    for k in data.keys():
        if k not in TOP_LEVEL_ALLOWED:
            stats["warnings"].append(
                f'Top-level junk key "{k}" (allowed: {", ".join(sorted(TOP_LEVEL_ALLOWED))})'
            )

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
        # First pass: collect globalids/aliases so object-ref lint can use them
        walk(wc, stats, "webcontent")

    return stats


def validate_file(path: Path, strict=False):
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return {
            "file": str(path),
            "ok": False,
            "errors": [f"JSON parse error: {e}"],
            "warnings": [],
            "stats": None,
        }

    stats = validate_data(data, strict)
    ok = len(stats["errors"]) == 0 and (not strict or len(stats["warnings"]) == 0)
    return {
        "file": str(path),
        "ok": ok,
        "errors": stats["errors"],
        "warnings": stats["warnings"],
        "stats": stats,
    }


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
