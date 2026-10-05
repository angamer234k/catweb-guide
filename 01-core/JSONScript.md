# JSONScript — Events, Actions & Parameter Shapes (Quick Reference)

**Primary authority:** SiteGPT V11 §5 (complete 16 events + 122 actions with exact `text` arrays and `t`/`l` slots).  
This file is a condensed survival guide.

## Hard invariants

1. Scripts are `"class":"script"` elements inside `webcontent` — never a top-level `"script"` key.
2. `text` is **always** an array of literal strings + parameter objects.
3. Control flow is **flat**: `If` / `Repeat` / `Iterate` never carry their own `"actions"` key. Body = siblings + matching `end` (id `25`).
4. Only top-level events (0–3, 5–16) or `Define function` (6) may have an `"actions"` array.
5. Variable names = numbers only (`{1}`, `{o!5}`, `{l!2}`).
6. Function params: prefer globals set before the call. Bare numeric `variable_overrides` break publishing.
7. Every string segment gets the `()` annotation for editor readability.
8. `t`/`l` are fixed per slot — copy from the authoritative table, never guess.

## Events (top-level content only)

| id | Event |
|----|-------|
| 0 | When website loaded |
| 1 | When button pressed |
| 2 | When key pressed |
| 3 | When mouse enters |
| 5 | When mouse leaves |
| 6 | Define function |
| 7 | When avataritem bought |
| 8 | When input submitted |
| 9 | When message received |
| 10 | When object changed |
| 11 | When mouse down on |
| 12 | When mouse up on |
| 13 | When button right clicked |
| 14 | When cross-site message received |
| 15 | When donation completed |
| 16 | When any key pressed |

## Most-used actions (remember the shapes)

- **11** Set variable → `{"t":"string","l":"variable"}` + `{"t":"string","l":"any"}`
- **31** Set property → property name + object + bare `{"t":"any"}`
- **88** Tween → property + object + bare `{"t":"any"}` + time + style + direction
- **10** Set text
- **8/9** Make invisible / visible
- **18/19/20/21/125/126** Comparisons — both sides `{"t":"string","l":"any"}`  
  (20 = greater, 21 = lower — do not swap)
- **22** Repeat n times · **23** Repeat forever · **25** end · **112** else
- **84** Get viewport size
- **30** Get text from input (`l:"input"`)
- **4** Redirect (`href:true`)
- **34/36** Cookie set/get (requires Cookies gamepass)
- **87** Run function (tuple always explicit array, even empty)
- **114** Run math function (no connector string between name and tuple)

## Two different “any” shapes

| Shape | Used by |
|-------|---------|
| Bare `{"t":"any"}` (no `l`) | Log, Warn, Error, Set prop value, Tween “to”, Set cookie |
| `{"t":"string","l":"any"}` | Set variable, table entry, insert, return, **all comparison operands** |

## Full table

The complete exact `text` arrays for every confirmed event and action live in **SiteGPT V11 §5.5**.  
Do not invent IDs. Do not approximate parameter shapes.

When generating scripts, run the mental pre-emit sweep from SiteGPT §5.5c before outputting.
