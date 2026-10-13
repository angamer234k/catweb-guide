# JSONScript — Events, Actions & Parameter Shapes (Quick Reference)

**Targeting CatWeb v2.19.0.0**  
**Primary authority:** SiteGPT V11 §5 + live v2.19 action IDs.

## Hard invariants

1. Scripts are `"class":"script"` elements inside `webcontent` — never a top-level `"script"` key.
2. `text` is **always** an array of literal strings + parameter objects.
3. Control flow is **flat**: `If` / `Repeat` / `Iterate` never carry their own `"actions"` key. Body = siblings + matching `end` (id `25`).
4. Only top-level events or `Define function` may have an `"actions"` array.
5. Variable names = numbers only (`{1}`, `{o!5}`, `{l!2}`).
6. Function params: prefer globals set before the call.
7. `t`/`l` are fixed per slot — copy from the authoritative table, never guess.

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

## Script limits (v2.19+)

- **90** events per script (was 30)
- **360** actions per event (was 120)

## Most-used actions

| id | Action | Notes |
|----|--------|-------|
| 11 | Set variable | `{"t":"string","l":"variable"}` + `{"t":"string","l":"any"}` |
| 10 | Set text | |
| 8 / 9 | Make invisible / visible | |
| 31 | Set property | |
| 88 | Tween | |
| 18–21, 125–126 | Comparisons | both sides `{"t":"string","l":"any"}` |
| 22 / 23 / 25 / 112 | Repeat / forever / end / else | flat |
| 84 | Get viewport size | |
| 30 | Get text from input | |
| 4 | Redirect | |
| 34 / 36 | Cookie set/get | needs gamepass |
| 87 | Run function | tuple always array |

## New in v2.19 — Attributes & Mouse

| id | Action | Approximate shape |
|----|--------|-------------------|
| **138** | Set \<attribute\> of \<object\> to \<any?\> | attribute name + object + value |
| **139** | Get \<attribute\> of \<object\> → \<variable\> | attribute name + object → variable |
| **140** | Get all attributes of \<object\> → \<table\> | object → table variable |
| **135** | Set mouse icon to \<id?\> | asset id (image) |
| **136** | Hide mouse cursor | no params |
| **137** | Show mouse cursor | no params |

Exact `text` arrays from live dump:

```json
// 139 Get attribute
{"id":"139","text":["Get",{"t":"string","l":"attribute"},"of",{"t":"object"},"→",{"t":"string","l":"variable"}]}

// 138 Set attribute
{"id":"138","text":["Set",{"t":"string","l":"attribute"},"of",{"t":"object"},"to",{"t":"any","l":"any?"}]}

// 140 Get all attributes
{"id":"140","text":["Get all attributes of",{"t":"object"},"→",{"t":"string","l":"table"}]}

// 135 Set mouse icon
{"id":"135","text":["Set mouse icon to",{"t":"id","assetbrowser":"image","l":"id?"}]}

// 136 Hide mouse
{"id":"136","text":["Hide mouse cursor"]}

// 137 Show mouse
{"id":"137","text":["Show mouse cursor"]}
```

## Two different “any” shapes

| Shape | Used by |
|-------|---------|
| Bare `{"t":"any"}` | Log, Warn, Set prop, Tween “to”, Set cookie |
| `{"t":"string","l":"any"}` | Set variable, comparisons, table ops |
| `{"t":"any","l":"any?"}` | Set attribute value (v2.19) |

## Full table

Complete exact shapes for older actions live in **SiteGPT V11 §5.5**.  
Do not invent IDs. Do not approximate parameter shapes.

When generating scripts, run the pre-emit sweep before outputting.
