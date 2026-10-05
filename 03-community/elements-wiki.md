# Elements (Community / Wiki Naming)

The Fandom wiki uses slightly friendlier names.  
This table maps them to the exact JSON `class` values used by AI generation.

## Regular / visual elements

| Wiki name | JSON `class` | Notes |
|-----------|--------------|-------|
| Frame | `Frame` | Container |
| Text | `TextLabel` | Static text |
| Image | `ImageLabel` | Image |
| Link | `TextButton?link` | Navigating button |
| Button | `TextButton` | Clickable |
| Donation | `TextButton?transfer` | Robux purchase prompt |
| Input | `TextBox` | User text input |
| Scrollable Frame / Scroller | `ScrollingFrame` | Scrollable container |
| Script | `script` | Logic (non-visual) |
| Folder | `Folder` | Organizer only |

Also exist in the full schema: `ImageButton`, `ImageButton?link`, `TextButton?avataritem`.

## Styling elements (must be children of a visual element)

| Wiki name | JSON `class` |
|-----------|--------------|
| Outline | `UIStroke` |
| Corner | `UICorner` |
| List | `UIListLayout` |
| Grid | `UIGridLayout` |
| Aspect Ratio | `UIAspectRatioConstraint` |
| Constraint | `UISizeConstraint` |
| Gradient | `UIGradient` |
| Padding | `UIPadding` |

(Plus `UIFlexItem` in the modern schema.)

## Important for AIs

Always use the exact JSON class names from SiteGPT / UIGPT.  
Wiki names are only for human conversation.
