# CatWeb Update History (Summary)

## v2.19.0.0 — Unlimited Update (Oct 11, 2026)

**Official event:** https://www.roblox.com/events/2082717428307067527

### 🟢 Added

| Feature | Details |
|---------|---------|
| **Shadow** styling element | `UIShadow` — BlurRadius, Color, Offset, Spread, Transparency, z_index |
| **Per-corner radii** | `UICorner` now has `radius_top_left`, `radius_top_right`, `radius_bottom_left`, `radius_bottom_right` |
| **Attributes** | Custom key-value pairs on elements (max 8). Scriptable via Get/Set/Get-all |
| **Mouse cursor control** | Set mouse icon, Hide mouse cursor, Show mouse cursor |
| **Middle / Top / Bottom Image** | New image properties |
| **Analytics** | Session time, popular pages, reach, demographics, etc. |

### New actions (authoritative IDs)

| ID | Action |
|----|--------|
| `138` | Set \<attribute\> of \<object\> to \<any?\> |
| `139` | Get \<attribute\> of \<object\> → \<variable\> |
| `140` | Get all attributes of \<object\> → \<table\> |
| `135` | Set mouse icon to \<id?\> |
| `136` | Hide mouse cursor |
| `137` | Show mouse cursor |

### 🟡 Changed

- **Object Limit removed** → replaced by **Cost Limit** (elements + styling + events + actions)
- Script limits: **30 → 90 events**, **120 → 360 actions/event**
- ScrollableFrame Color / Transparency / Thickness now scriptable
- CatWeb TV UI updated

### 🔵 Fixed

- "Is left mouse button down" now correctly detects mobile / console presses

### Rollout

- Cost Limit available immediately for **Premium**
- Free users over the following weeks

---

## Earlier milestones

| Version | Date | Highlights |
|---------|------|------------|
| v2.15 | ~Dec 2025 | Collaboration (Beta), copy/paste, mobile UX, higher var data |
| v2.14 | ~Nov 2025 | Hallway event, multi-element edit, Easy Styling |
| v2.10.0 | Mar 2025 | Anniversary — milestone badges, Gradient, Padding, Tooltip |
| Public | Mar 2024 | Launch |

When the game updates again, check `catweb://whats-new` first, then update this file + `VERSION.md`.
