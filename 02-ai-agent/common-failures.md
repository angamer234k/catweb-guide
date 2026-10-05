# Common Failures (Fix These Before Emitting)

These are the real reasons sites fail to import or publish.  
Check every generated site against this list.

## Instant import death (`[INVALIDATED]`)

| Mistake | Correct |
|---------|---------|
| `"layout_order": "1"` | `"order": "1"` |
| `"cell_size": "{0,200},{0,150}"` on UIGridLayout | `"size": "{0,200},{0,150}"` |
| Any unknown property key | Only keys listed for that class in SiteGPT / UIGPT |
| Top-level `"script"` key | `"class": "script"` element inside `webcontent` |
| Control-flow action with its own `"actions": [...]` | Flat siblings + `end` (id 25) |
| Invented action `id` | Only IDs from §5.5 of SiteGPT |

## Publish fails (imports fine, then refuses to publish)

| Mistake | Correct |
|---------|---------|
| `variable_overrides` with bare numbers (`"1"`, `"2"`) | Prefer no formal params — pass via globals |
| Wrong `t`/`l` on a parameter slot | Copy the exact shape from the block table |
| Confusing the two “any” shapes | Bare `{"t":"any"}` vs `{"t":"string","l":"any"}` — they are not interchangeable |
| Swapped comparison ids | `20` = greater than, `21` = lower than |

## Visual / layout defects (valid JSON, looks broken)

| Mistake | Correct |
|---------|---------|
| Fixed-width card left-aligned | `position` x = `"{0.5,...}"` + `anchor` = `"0.5,0"` |
| Padding faked with position + smaller size | Always use a `UIPadding` child |
| Sections overlapping | Parent with Vertical `UIListLayout` + `"order"` on children |
| Chips with fixed width + `auto_y` | Chips use `size: "auto"` |
| Nested ScrollingFrame inside navbar | Navbar and body scroller must be **siblings** |

## Scripting gotchas

| Mistake | Correct |
|---------|---------|
| Word-named variables (`count`, `score`) | Numbers only: `{1}`, `{40}`, `{o!5}` |
| Object ref by `alias` instead of `globalid` | Always `globalid` |
| `Define function` nested inside an event | Top-level sibling of events |
| Missing `end` for `If` / `Repeat` / `Iterate` | Exactly one matching `end` per opener |
| Decoder used on short strings | Only for genuinely long text that risks filtering |

## Asset / text mistakes

| Mistake | Correct |
|---------|---------|
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
