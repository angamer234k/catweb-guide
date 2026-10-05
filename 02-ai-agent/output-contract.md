# Output Contract (Hard Rules for AI Agents)

**This is non-negotiable.** Every time you generate a CatWeb site, your response must obey these rules.

## 1. Deliverable format

- Output **exactly one** valid JSON object (the full site).
- Never output Lua, JavaScript, HTML, Markdown code fences around the JSON, or explanations mixed into the JSON.
- The JSON must parse cleanly. No trailing commas, no comments (`//` or `/* */`).

## 2. Top-level shape

```json
{
  "favicon": "numericAssetId",
  "title": "Short plain title",
  "background": "#rrggbb",
  "webcontent": [ /* elements */ ]
}
```

Optional: `thumbnail_id`, `thumbnail`.

## 3. Scalar values

- **Every** number, boolean, and null is a **quoted string**.
  - Correct: `"font_size": "16"`, `"visible": "true"`, `"z_index": "10"`
  - Wrong: `"font_size": 16`, `"visible": true`

## 4. Identifiers

- `globalid`: exactly 2–3 characters from `[A-Za-z0-9]`, unique across the whole file.
- `alias`: unique, lowercase, descriptive (editor-only). No placeholders like `"alias1"`.

## 5. Properties

- Only use property keys documented in SiteGPT V11 / UIGPT.md for that `class`.
- Forbidden keys that cause instant `[INVALIDATED]`:
  - `layout_order` → use `"order"`
  - `cell_size` → use `"size"` on UIGridLayout
  - any invented key (`padding`, `margin`, `gap`, `border-radius`, etc.)

## 6. Scripts

- Scripts are elements: `"class": "script"` inside `webcontent`.
- Never a top-level `"script"` key.
- Action/event `id`s must come from the authoritative table only.
- Control flow (`If`, `Repeat`, `Iterate`) is **flat** — no nested `"actions"` key. Body = siblings + matching `"end"` (id `25`).
- Variable names are **numbers only** (`{1}`, `{o!5}`, `{l!2}`).

## 7. Text & assets

- No emoji or special Unicode arrows/directional glyphs in site text. Use the icon library.
- Never invent Roblox asset IDs. Use only the confirmed ones in Assets.md.

## 8. When you cannot produce a valid site

If the request would require inventing undocumented actions, properties, or asset IDs, say so clearly instead of guessing.

---

**Full details + examples:** `01-core/SiteGPT-V11.md`  
**Quick skill file:** `02-ai-agent/SKILL.md`
