# 04-tools

## validate.py / validate.js
- Object counts, forbidden keys, non-string scalars
- **Action `text` slot counts** from SiteGPT table (`INVALID_ACTION_ARGS`) — catches the publish-hang class of bugs
- globalid charset on elements **and** script actions
- Object-ref warnings (alias vs globalid)
- Filter-word warnings (`paste`, etc.)
- Top-level junk keys

```bash
python 04-tools/validate.py site.json
python 04-tools/validate.py site.json --strict
```

## repair.py / repair.js
Conservative only. **Does not** rewrite action shapes (those must be regenerated).

Safe fixes: keys, scalars, globalids, root shape, flatten nested control-flow.

```bash
python 04-tools/repair.py site.json          # print report + JSON if changed
python 04-tools/repair.py site.json --write  # write *.repaired.json
```

If schema is fine → `NO_REPAIR_NEEDED`.
