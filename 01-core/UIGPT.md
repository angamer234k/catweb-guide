# UIGPT — Element Schema & Layout (Quick Reference)

**Primary authority:** SiteGPT V11 (full detailed schemas, examples, and edge cases).  
This file is a condensed merged view for fast lookup.

## Top-level site object

```json
{
  "favicon": "numericAssetId",
  "title": "Tab Title",
  "background": "#rrggbb",
  "webcontent": [ /* one or more root elements */ ],
  "thumbnail_id": "optional",
  "thumbnail": "rbxassetid://optional"
}
```

All scalar values are **quoted strings**.

## Common properties (almost every visual element)

| Property | Format / notes |
|----------|----------------|
| `class` | Element type |
| `globalid` | 2–3 alphanumeric, unique |
| `alias` | unique descriptive label (editor only) |
| `position` | `"{xScale,xOffset},{yScale,yOffset}"` |
| `size` | UDim2 or `"auto"` / `"auto_x"` / `"auto_y"` |
| `width` / `height` | UDim (used with auto_y / auto_x) |
| `anchor` | `"x,y"` (0–1) |
| `background_color` | `"#rrggbb"` |
| `background_transparency` | `"0"`–`"1"` |
| `visible` | `"true"` / `"false"` |
| `z_index` | string integer |
| `rotation` | degrees string |
| `tooltip` | string |
| `children` | array |
| `order` | integer string (for LayoutOrder) |

## Visual classes

- `Frame` — container
- `TextLabel` — static text
- `TextButton` — clickable (+ `auto_color`)
- `TextButton?link` — navigates (`href`, `new_tab`)
- `TextButton?transfer` — Roblox purchase prompt (`product`, `product_type`, `thanks_href`)
- `TextButton?avataritem` — avatar item purchase
- `ImageLabel` / `ImageButton` / `ImageButton?link`
- `TextBox` — input (`placeholder`, `editable`, `multiline`)
- `ScrollingFrame` — (`canvassize`: `"auto_y"` / `"auto_x"` / `"auto_xy"`, never bare `"auto"`)

## Non-visual

- `script` — logic (`enabled`, `content`)
- `Folder` — organizer only

## Styling modifiers (children of visual elements only)

`UICorner` · `UIStroke` · `UIPadding` · `UIListLayout` · `UIGridLayout` · `UIGradient` · `UIAspectRatioConstraint` · `UISizeConstraint` · `UIFlexItem`

**Critical key names:**
- Layout order → `"order"` (never `layout_order`)
- Grid cell size → `"size"` (never `cell_size`)
- Gradient colors → stringified array **without** `#` inside the stops

## Layout patterns that actually work

1. **Sticky header + scrolling body**  
   Root `Frame {1,0},{1,0}`  
   → Navbar sibling `Frame {1,0},{0,56}` (z_index 10)  
   → Body `ScrollingFrame {1,0},{1,-56}` pos `{0,0},{0,56}` canvassize `"auto_y"`

2. **Vertical stack**  
   Parent with `UIListLayout` direction Vertical + `sort:"LayoutOrder"`  
   Children all at `{0,0},{0,0}` with integer `"order"`

3. **Center a fixed-width card**  
   `position` x = `"{0.5,0}"` + `anchor` = `"0.5,0"`

4. **Padding**  
   Always a `UIPadding` child. Never fake it with position + smaller size.

Full examples, font list, responsive patterns, and every property table → **SiteGPT V11**.
