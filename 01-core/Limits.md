# Platform Limits & Monetization

**Source of truth merged from SiteGPT V11 + Mailo docs + wiki.**

## Element & Runtime Limits

| Item                        | Free     | Premium          |
|-----------------------------|----------|------------------|
| Elements (all types count)  | 100      | 400              |
| Sites / free domains        | 1        | 3                |
| Subdomains                  | 3        | 5                |
| Pages per site              | 15       | 30               |
| Runtime objects (incl. Duplicated) | 1,000 | 1,000         |
| Actions per event           | 120      | 120              |
| Events per script           | 30       | 30               |
| Actions per script (total)  | 3,600    | 3,600            |
| Tuple parameters            | 6        | 6                |
| Concurrent sounds           | 150      | 150              |
| Broadcast message size      | 979 bytes| 979 bytes        |
| Page/site broadcast rate    | 5 / 2s   | 5 / 2s           |
| Cross-site broadcast rate   | 4 / 20s (uncached), 5 / 2s (cached) | same |
| Cookie storage              | 10 KB per site | same        |
| Cookie write rate           | ~1 / 0.05s | same           |

**Notes:**
- Every element type counts toward the limit: `UICorner`, `UIPadding`, `UIStroke`, `UIGradient`, `UIListLayout`, `UIGridLayout`, constraints, `UIFlexItem`, `Folder`, and `script` nodes all count as 1.
- Events and action blocks *inside* a script do **not** count — only the `script` element itself does. This is a key budgeting lever.
- Text limits: ~20,000 characters per text element before TEXT_OVERLOAD; 200,000 across all text elements on the page.

## Monetization

| Item                  | Price              | What you get |
|-----------------------|--------------------|--------------|
| **Premium**           | 299 Robux (~$3.74) | 400 elements, 3 free sites, 5 subdomains, 30 pages/site, custom themes (up to 10), Premium chat tag + profile icon. **Does NOT include Cookies gamepass.** |
| **Cookies Gamepass**  | 80 Robux (~$0.99)  | Enables all Cookie actions (`Set`/`Get`/`Increase`/`Delete`). 10 KB storage per site. Required for any persistent local storage. |
| **Extra Domain**      | ~29 Robux (varies by region) | One additional domain. |

Premium local page: `catweb://premium`

## Other Hard Limits

- No server-side scripting or Datastores. Everything runs client-side on the visitor’s machine.
- Landscape only — no portrait layouts.
- Broadcasts are visible to every visitor on the page (security implication for any relay/datastore patterns).
