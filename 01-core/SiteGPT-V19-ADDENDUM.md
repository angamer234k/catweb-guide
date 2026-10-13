# SiteGPT V11 — v2.19.0.0 Addendum (Unlimited Update)

This addendum patches the original SiteGPT V11 for CatWeb **v2.19.0.0**.  
Merge these sections into the main guide (or treat this file as authoritative for the new features).

---

## OUTPUT CONTRACT note

Core contract unchanged. New documented keys: `attributes`, `UIShadow`, per-corner radii, actions **135–140**.

---

## §2.1 — Common property added

| Property | Format | Notes |
|---|---|---|
| `attributes` | array | **v2.19+** Custom key-value pairs (max 8). See §2.1d |

### 2.1d Attributes (v2.19+)

```json
"attributes": [
  {
    "name":  { "value": "theme" },
    "value": { "value": "dark" }
  }
]
```

- Max **8** attributes per element.
- Script access: actions `138` (Set), `139` (Get), `140` (Get all).

---

## §2.7 — UICorner (expanded) + UIShadow (new)

### UICorner

```json
{
  "class": "UICorner",
  "globalid": "cr",
  "radius": "0,10",
  "radius_top_left": "0,24",
  "radius_top_right": "0,8",
  "radius_bottom_left": "0,8",
  "radius_bottom_right": "0,24"
}
```

| Property | Format |
|---|---|
| `radius` | UDim (uniform) |
| `radius_top_left` | UDim **v2.19+** |
| `radius_top_right` | UDim **v2.19+** |
| `radius_bottom_left` | UDim **v2.19+** |
| `radius_bottom_right` | UDim **v2.19+** |

### UIShadow (v2.19+)

```json
{
  "class": "UIShadow",
  "globalid": "sh",
  "blur_radius": "0,12",
  "shadow_color": "#000000",
  "shadow_transparency": "0.55",
  "shadow_offset": "{0,0},{0,6}",
  "shadow_spread": "{0,0},{0,0}",
  "z_index": "0"
}
```

Must be a **child** of the visual element it shadows.

---

## §5.2 / §8 — Script & platform limits

| Item | Old | v2.19+ |
|---|---|---|
| Events per script | 30 | **90** |
| Actions per event | 120 | **360** |
| Actions per script | 3,600 | **32,400** |
| Object Limit | 100 / 400 | **Cost Limit** (∞ practical) |
| Attributes per element | — | **8** |

Cost Limit = elements + styling elements + events + actions.  
At/over Cost Limit → edit OK, **publish blocked**.

---

## §5.5 — New actions (exact shapes)

| `id` | Action | Exact `text` array |
|---|---|---|
| `135` | Set mouse icon | `["Set mouse icon to", {t:id, assetbrowser:image, l:id?}]` |
| `136` | Hide mouse cursor | `["Hide mouse cursor"]` |
| `137` | Show mouse cursor | `["Show mouse cursor"]` |
| `138` | Set attribute | `["Set", {t:string, l:attribute}, "of", {t:object}, "to", {t:any, l:any?}]` |
| `139` | Get attribute | `["Get", {t:string, l:attribute}, "of", {t:object}, "→", {t:string, l:variable}]` |
| `140` | Get all attributes | `["Get all attributes of", {t:object}, "→", {t:string, l:table}]` |

---

## Example

See `02-ai-agent/examples/v219_shadow_attributes.json`.
