# CatWeb Update History (Summary)

High-level changelog notes useful for AIs and humans.  
Full changelogs live on the Fandom wiki and in-game (`catweb://whats-new`).

## Upcoming: Unlimited Update (Oct 11, 2026)

**Official event:** https://www.roblox.com/events/2082717428307067527  
Sneak peeks from HumanCat222 (@sneak peeks channel)

### Confirmed changes

| Feature | Details |
|---------|---------|
| **Object Limit → Cost Limit** | Hard object limit (100 free / 400 Premium) is **removed**. Replaced by a single **cost** limit calculated from: elements + styling elements + events + actions in scripts. Designed to be high enough for normal use. |
| **Event limit** | 30 → **90** |
| **Action limit (per event)** | 120 → **360** |
| **Premium early access** | Premium users get the new Cost Limit system at launch. Free users roll out over the following week. All other Premium perks (pages, domains, themes, etc.) stay. |
| **Publishing behavior** | Reaching the Cost Limit still lets you edit & collaborate, but **blocks publishing**. Editor only hard-stops if you go *significantly* over. |
| **Attributes** | New custom **Attributes** on elements (key-value pairs, visible in properties panel). |
| **Individual corner radii** | `UICorner` can now set TopLeft / TopRight / BottomLeft / BottomRight independently. |
| **Shadows** | New **Shadow** styling element (BlurRadius, Color, Offset, Spread, Transparency, Layer). |

### What this means for AI agents

- Old hard caps of 100/400 elements no longer apply after the update.
- Prefer generating richer sites when the Cost Limit is live.
- New property keys / element classes (Attributes, per-corner radii, Shadow) must be confirmed in the live editor before using them in generated JSON — do **not** invent shapes until SiteGPT / JSONScript is updated.
- Keep watching `catweb://whats-new` on release day.

---

## Early history

- **Public release:** March 2024 (Anniversary: March 24)
- **Dev start:** ~April 2024
- First updates (v1.0.x / v1.1) added donation buttons, basic editor improvements, middle-click new tab, etc.

## Notable 2.x milestones

| Version | Approx date | Highlights |
|---------|-------------|------------|
| **v2.9.x** | early 2025 | Script editor improvements, output panel, keyboard shortcuts |
| **v2.10.0** | Mar 25, 2025 | **Anniversary Update** — Milestone badges, Tooltip, Rich/Wrap/Truncate text, Gradient + Padding styling, better mobile resize, search spellcheck |
| **v2.12–2.13** | mid 2025 | Various quality & block improvements |
| **v2.14** | ~Nov 2025 | **Hallway** event, direct table entry access (`{table.entry}`), multi-element property editing, Easy Styling category, F5 / Ctrl+F5 test, Ctrl+A select all |
| **v2.15** | ~Dec 2025 | **Collaboration (Beta)** (up to 10 people), copy/cut/paste elements across sites, major mobile editor UX, higher variable data limit (~5 MB), higher broadcast rate |

## Other notes

- Old script editor was replaced (Feb 2025 era).
- Cookie system received dedicated improvements.
- Broadcast size / rate limits have been raised over time (see `01-core/Limits.md`).
- **2026 Downage:** short (~2 day) period where the game was under Roblox review.

When the game updates, prefer checking:

1. `catweb://whats-new`
2. In-game block palette
3. Then update this file + `VERSION.md`
