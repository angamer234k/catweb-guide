# Common Failure Modes

Mistakes that look fine locally but break import, publish, or runtime.

## Import dies immediately

| Mistake | Correct |
|---------|--------|
| Invented action / event `id` | Only IDs from SiteGPT §5.5 / JSONScript.md |
| Wrong `t` / `l` on a slot | Copy exact shape from the table |
| Top-level `"script"` key | `"class": "script"` element inside `webcontent` |
| Control-flow action with its own `"actions": [...]` | Flat siblings + `end` (id 25) |
| Invented action `id` | Only IDs from §5.5 of SiteGPT |

## Publish fails (imports fine, then refuses to publish)

| Mistake | Correct |
|---------|--------|
| `variable_overrides` with bare numbers (`"1"`, `"2"`) | Prefer no formal params — pass via globals |
| Wrong `t`/`l` on a parameter slot | Copy the exact shape from the block table |
| Confusing the two “any” shapes | Bare `{"t":"any"}` vs `{"t":"string","l":"any"}` — they are not interchangeable |
| Swapped comparison ids | `20` = greater than, `21` = lower than |
| `()` labels in `text` literals (`"Set (1)"`, `"to (0)"`) | Bare connectives only: `"Set"`, `"to"` — **never** put the value in parentheses before the input slot |
| Accidental parentheses before a parameter the action shape does **not** expect | **Publish fails silently.** Always match the exact `text` array shape. No annotation parentheses ever. |

**Hard rule on parentheses:**  
If the official shape is  
`["Set", {"t":"string","l":"variable"}, "to", {"t":"string","l":"any"}]`  
then the JSON **must** look exactly like that.  
Putting `"Set (1)"` or `"to (hello)"` (or any parentheses around the value) makes publish fail with **zero error message**.

## Visual / layout defects (valid JSON, looks broken)

| Mistake | Correct |
|---------|--------|
| Fixed-width card left-aligned | `position` x = `"{0.5,...}"` + `anchor` = `"0.5,0"` |
| Padding faked with position + smaller size | Always use a `UIPadding` child |
| Sections overlapping | Parent with Vertical `UIListLayout` + `"order"` on children |
| Chips with fixed width + `auto_y` | Chips use `size: "auto"` |
| Nested ScrollingFrame inside navbar | Navbar and body scroller must be **siblings** |

## Scripting gotchas

| Mistake | Correct |
|---------|--------|
| Word-named variables (`count`, `score`) | Numbers only: `{1}`, `{40}`, `{o!5}` |
| Object ref by `alias` instead of `globalid` | Always `globalid` |
| `Define function` nested inside an event | Top-level sibling of events |
| Missing `end` for `If` / `Repeat` / `Iterate` | Exactly one matching `end` per opener |
| Decoder used on short strings | Only for genuinely long text that risks filtering |

## Asset / text mistakes

| Mistake | Correct |
|---------|--------|
| Invented image/sound asset ID | Only the 84 icons + 8 sounds in Assets.md |
| Emoji or special arrows in text | Use icon library |
| Hex with `#` inside gradient stops | Gradient stops drop the `#` |
| Hex without `#` in element properties | Element properties keep the `#` |

---

**Pre-emit checklist (from SiteGPT §5.5c):**

1. Every `id` exists in the authoritative table and parameter shapes match exactly.
2. Top-level `content` entries are only events or `Define function`.
3. No control-flow action has a nested `"actions"` key.
4. Every opener has exactly one matching `end`.
5. Comparison direction matches the id (`20` vs `21`).
6. Tuples are always explicit arrays, even when empty.
7. Every `globalid` is unique and charset-safe; object refs use `globalid`.
8. No `()` value labels in `text` literals — bare connectives only.
