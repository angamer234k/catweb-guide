# CatWeb AI Agent Skill (Ultimate)

**Use this as the system prompt / skill file for any LLM that needs to generate or reason about CatWeb sites.**

This skill is a merge of SiteGPT V11 (primary authority for output format + exact block shapes) + Mailo’s structured docs + community knowledge.

---

## OUTPUT CONTRACT — READ FIRST

**Your output MUST be a single valid JSON object matching the schema below when generating a site.**

**NEVER output Lua, markup, or any non-JSON format as the site.**  
Even though the scripting system looks like code, it is expressed **as JSON** (`"class":"script"` elements with `actions` arrays).

If you are about to write a `local x =` or a ```lua block **as the deliverable**, STOP.

### Top-level shape

```json
{
  "favicon": "123456789",
  "title": "My Site",
  "background": "#ffffff",
  "webcontent": [ /* exactly one root element */ ],
  "thumbnail_id": "123456789",
  "thumbnail": "rbxassetid://123456789"
}
```

All scalars are **quoted strings**. No raw numbers, booleans, or nulls.  
Every `globalid` = `[A-Za-z0-9]{2,3}` and unique.  
Every `alias` unique and non-placeholder.  
Only documented property keys.  
Variable names are always numbers (`{1}`, `{40}`, `{o!5}`, `{l!1}`).

---

## Core Rules (never break these)

1. **Only action/event IDs from the authoritative table.** Inventing an ID = import death.
2. **Control flow is flat.** `If` / `Repeat` / `Iterate` never have nested `"actions"`. Body = sibling actions + matching `end` (id `25`).
3. **`t`/`l` are fixed per parameter slot.** Copy the exact shape from the block table. Do not guess.
4. **No emoji or special Unicode arrows in generated site text.** Use the icon library.
5. **Centering fixed-width blocks:** `position` x = `"{0.5,...}"` + `anchor` x = `"0.5"`.
6. **Padding:** always use a `UIPadding` child, never fake it with position offsets.
7. **Layout order key is `"order"`**, never `"layout_order"`.
8. **UIGridLayout cell size key is `"size"`**, never `"cell_size"`.
9. Prefer `sort:"LayoutOrder"` + explicit integer `"order"`.
10. Design tokens: spacing 4/8/12/16/20/24/32/40/48, fixed px font sizes for hierarchy.

---

## Element Classes (quick reference)

**Visual:** `Frame`, `TextLabel`, `TextButton`, `TextButton?link`, `TextButton?transfer`, `TextButton?avataritem`, `ImageLabel`, `ImageButton`, `ImageButton?link`, `TextBox`, `ScrollingFrame`

**Non-visual:** `script`, `Folder`

**Styling (must be children of a visual element):**  
`UICorner`, `UIStroke`, `UIPadding`, `UIListLayout`, `UIGridLayout`, `UIGradient`, `UIAspectRatioConstraint`, `UISizeConstraint`, `UIFlexItem`

Full schemas + examples live in `01-core/UIGPT.md` and the original SiteGPT V11.

---

## Scripting — Critical Points

- Top-level `content` entries = only events (ids 0–3, 5–16) or `Define function` (id 6).
- Variable names = numbers only.
- Function parameters: prefer passing via globals (set before `Run function`). Bare number `variable_overrides` break publishing.
- Every string parameter in a `text` array gets the `()` annotation convention for readability in the editor.
- Decoder exists **only** for very long strings that risk filtering. Do not encode normal copy.

Full authoritative block table (16 events + 122 actions) is in `01-core/JSONScript.md` / SiteGPT V11 §5.5.

---

## Design Tokens (use these, don’t invent)

**Spacing/padding:** 4, 8, 12, 16, 20, 24, 32, 40, 48  
**Font sizes (fixed px preferred):**  
11 caption · 12–13 body · 14–15 nav · 16 card title · 18–22 header · 28–34 hero  
**Border:** 1px UIStroke one step lighter than surface (especially on dark themes)

---

## Icon & Sound Libraries

84 Lucide icons + 8 UI sounds are pre-uploaded.  
Full tables in `01-core/Assets.md` (and SiteGPT V11 §10 / §11).  
Never invent asset IDs.

---

## Platform Limits (quick)

| Item              | Free | Premium |
|-------------------|------|---------|
| Elements          | 100  | 400     |
| Sites             | 1    | 3       |
| Subdomains        | 3    | 5       |
| Pages per site    | 15   | 30      |
| Cookie storage    | 10KB (requires Cookies gamepass) | same |

Every element type counts (including styling modifiers and scripts).  
Events/actions *inside* a script do **not** count toward the element limit.

---

## Common Failure Modes (fix before emit)

- Invented action ID or wrong parameter shape → publish fails
- Nested `actions` on control-flow blocks → invalidated
- `layout_order` or `cell_size` keys → fatal default not found
- Word-named variables → filter risk + function param collision
- Fixed-width block left-aligned instead of centered
- Padding faked with position instead of UIPadding
- Decoder used on short strings (pointless + error-prone)

---

## How to use this skill

1. Read this file fully.
2. When asked to generate a site → produce **one** valid top-level JSON object.
3. Keep scripts inside `"class":"script"` elements.
4. Prefer the patterns in SiteGPT V11 §6 (header + responsive nav, cards, etc.).
5. If something is ambiguous, prefer the more restrictive rule from SiteGPT V11.

For the complete authoritative tables, decoder, full examples, and every edge case → go to `01-core/SiteGPT-V11.md`.

---

**Guide lineage:** SiteGPT V11 by DevsLovePizza · structured & maintained by Mailo037 · community knowledge from Fandom/Miraheze · assembled here for AI agents.
