# Platform Limits & Monetization

**Targeting CatWeb v2.19.0.0 (Unlimited Update)**

## Cost Limit system (v2.19+)

The old hard Object Limit (100 free / 400 Premium) is **removed**.

Replaced by a single **Cost Limit** calculated from:
- Number of elements
- Styling elements
- Events
- Actions in scripts

| Behavior | Effect |
|----------|--------|
| Under Cost Limit | Normal edit + publish |
| At / over Cost Limit | Can still edit & collaborate, **cannot publish** |
| Significantly over | Editor may hard-stop |

- **Premium** users get Cost Limit at launch (Oct 11 2026)
- Free users roll out over the following weeks
- Designed to be high enough for normal use

## Script limits (v2.19+)

| Item | Old | New |
|------|-----|-----|
| Events per script | 30 | **90** |
| Actions per event | 120 | **360** |
| Max actions per script | 3,600 | **32,400** |

## Other limits (unchanged / still relevant)

| Item | Free | Premium |
|------|------|---------|
| Sites / free domains | 1 | 3 |
| Subdomains | 3 | 5 |
| Pages per site | 15 | 30 |
| Runtime objects (incl. Duplicated) | ~1,000 | ~1,000 |
| Tuple parameters | 6 | 6 |
| Concurrent sounds | 150 | 150 |
| Broadcast message size | 979 bytes | 979 bytes |
| Page/site broadcast rate | 5 / 2s | 5 / 2s |
| Cookie storage | 10 KB per site | same |
| Attributes per element | **8 max** | **8 max** |

**Notes:**
- Every element type still counts toward cost: `UICorner`, `UIPadding`, `UIStroke`, `UIGradient`, `UIListLayout`, `UIGridLayout`, `UIShadow`, constraints, `UIFlexItem`, `Folder`, and `script` nodes.
- Events and action blocks *inside* a script do **not** count as separate elements — only the `script` element itself does.
- Text limits: ~20,000 characters per text element; 200,000 across all text on the page.

## Monetization

| Item | Price | What you get |
|------|-------|--------------|
| **Premium** | 299 Robux | 3 free sites, 5 subdomains, 30 pages/site, custom themes (up to 10), Premium chat tag + icon, **early Cost Limit access** |
| **Cookies Gamepass** | 80 Robux | Enables Cookie actions. 10 KB storage per site. |
| **Extra Domain** | ~29 Robux | One additional domain. |
