# UIGPT — Element Schema & Layout (Quick Reference)

**Targeting CatWeb v2.19.0.0 (Unlimited Update)**  
**Primary authority:** SiteGPT V11 + live v2.19 shapes.

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
| `attributes` | array of attribute objects (max 8) — **v2.19+** |

## Attributes (v2.19+)

```json
"attributes": [
  {
    "name":  { "value": "Attribute 1" },
    "value": { "value": "some value" }
  }
]
```

- Max **8** attributes per element
- Scriptable via actions 138 / 139 / 140

## Visual classes

- `Frame` — container
- `TextLabel` — static text
- `TextButton` — clickable (+ `auto_color`)
- `TextButton?link` — navigates (`href`, `new_tab`)
- `TextButton?transfer` — Roblox purchase prompt
- `TextButton?avataritem` — avatar item purchase
- `ImageLabel` / `ImageButton` / `ImageButton?link`
- `TextBox` — input
- `ScrollingFrame` — (`canvassize`: `"auto_y"` / `"auto_x"` / `"auto_xy"`)

## Non-visual

- `script` — logic (`enabled`, `content`)
- `Folder` — organizer only

## Styling modifiers (children of visual elements only)

| Class | Key properties |
|-------|----------------|
| `UICorner` | `radius`, **`radius_top_left`**, **`radius_top_right`**, **`radius_bottom_left`**, **`radius_bottom_right`** (v2.19+) |
| `UIShadow` | **NEW v2.19** — see below |
| `UIStroke` | `stroke_color`, `stroke_thickness`, `stroke_transparency` |
| `UIPadding` | `top`, `bottom`, `left`, `right` |
| `UIListLayout` | `direction`, `padding`, `sort`, `alignment_*` |
| `UIGridLayout` | `size` (cell), `padding`, etc. |
| `UIGradient` | color stops **without** `#` |
| `UIAspectRatioConstraint` | |
| `UISizeConstraint` | |
| `UIFlexItem` | |

### UIShadow (v2.19+)

```json
{
  "class": "UIShadow",
  "globalid": "sF",
  "blur_radius": "1, 0",
  "shadow_color": "#ff0000",
  "shadow_transparency": "0.59",
  "shadow_offset": "{0, 3},{0, 3}",
  "shadow_spread": "{0, -5},{0, -5}",
  "z_index": "1"
}
```

### UICorner per-corner (v2.19+)

```json
{
  "class": "UICorner",
  "globalid": "'S",
  "radius": "0.1, 0",
  "radius_top_left": "1, 0",
  "radius_top_right": "0, 0",
  "radius_bottom_left": "1, 0",
  "radius_bottom_right": "0, 0"
}
```

**Critical key names:**
- Layout order → `"order"` (never `layout_order`)
- Grid cell size → `"size"` (never `cell_size`)
- Gradient colors → stringified array **without** `#` inside the stops

## Layout patterns that actually work

1. **Sticky header + scrolling body**  
   Root `Frame {1,0},{1,0}` → Navbar sibling + Body `ScrollingFrame`

2. **Vertical stack**  
   Parent with `UIListLayout` direction Vertical + `sort:"LayoutOrder"`

3. **Center a fixed-width card**  
   `position` x = `"{0.5,0}"` + `anchor` = `"0.5,0"`

4. **Padding**  
   Always a `UIPadding` child.

Full examples → **SiteGPT V11** + `02-ai-agent/examples/`.
