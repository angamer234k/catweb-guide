# Platform Limits & Monetization

**Source of truth merged from SiteGPT V11 + Mailo docs + wiki + Unlimited Update sneak peeks.**

> ⚠️ **Unlimited Update (Oct 11, 2026)** changes the core object/event/action limits.  
> Until the update fully rolls out, the old numbers still apply for free users.

## Current (pre-Unlimited) limits

| Item | Free | Premium |
|------|------|---------|
| Elements (all types count) | 100 | 400 |
| Sites / free domains | 1 | 3 |
| Subdomains | 3 | 5 |
| Pages per site | 15 | 30 |
| Runtime objects (incl. Duplicated) | 1,000 | 1,000 |
| Actions per event | 120 | 120 |
| Events per script | 30 | 30 |
| Actions per script (total) | 3,600 | 3,600 |
| Tuple parameters | 6 | 6 |
| Concurrent sounds | 150 | 150 |
| Broadcast message size | 979 bytes | 979 bytes |
| Page/site broadcast rate | 5 / 2s | 5 / 2s |
| Cross-site broadcast rate | 4 / 20s (uncached), 5 / 2s (cached) | same |
| Cookie storage | 10 KB per site | same |
| Cookie write rate | ~1 / 0.05s | same |

**Notes:**
- Every element type counts toward the limit: `UICorner`, `UIPadding`, `UIStroke`, `UIGradient`, `UIListLayout`, `UIGridLayout`, constraints, `UIFlexItem`, `Folder`, and `script` nodes all count as 1.
- Events and action blocks *inside* a script do **not** count — only the `script` element itself does.
- Text limits: ~20,000 characters per text element before TEXT_OVERLOAD; 200,000 across all text elements on the page.

## After Unlimited Update (Oct 11, 2026+)

| Item | New value |
|------|-----------|
| Object Limit | **Removed** (∞) — replaced by **Cost Limit** |
| Event limit | **90** (was 30) |
| Action limit per event | **360** (was 120) |
| Cost Limit | Single budget based on: elements + styling elements + events + actions. High enough for normal use. |

- Reaching Cost Limit → can still edit & collaborate, **cannot publish**.
- Going *significantly* over → editor may stop working.
- **Premium** gets Cost Limit system at launch; free users over the following week.
- All other Premium perks (extra pages/domains, custom themes, chat tag, etc.) remain.

## Monetization

| Item | Price | What you get |
|------|-------|--------------|
| **Premium** | 299 Robux (~$3.74) | 3 free sites, 5 subdomains, 30 pages/site, custom themes (up to 10), Premium chat tag + profile icon, **early Cost Limit access** |
| **Cookies Gamepass** | 80 Robux (~$0.99) | Enables all Cookie actions. 10 KB storage per site. Required for any persistent local storage. |
| **Extra Domain** | ~29 Robux (varies) | One additional domain. |

## New features coming with Unlimited (not yet in JSON schema)

These are confirmed in sneak peeks but **do not invent JSON keys** until the live editor / SiteGPT is updated:

- **Attributes** — custom key-value pairs on elements
- **Per-corner UICorner** — TopLeft / TopRight / BottomLeft / BottomRight
- **Shadow** styling element — BlurRadius, Color, Offset, Spread, Transparency, Layer
