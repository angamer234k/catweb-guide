# What is CatWeb? (Overview for AIs & Humans)

**CatWeb** is a Roblox game created by **HumanCat222** (@CcXxiiHuman_C4t) where players build fully functional 2D websites inside a browser simulation.

- **TLD:** `.rbx` (exclusive to the game — not a real internet domain)
- **Inspiration:** Google Chrome (explicit parody — “Do not take it seriously”)
- **Public release:** March 2024 (Anniversary: March 24)
- **Development start:** ~April 2024
- **Scripting:** Visual block-based language (similar to Scratch), stored/shared as special JSON
- **Scale:** hundreds of thousands of registered sites (community estimates have cited ~730k at peaks)

## Core features

- In-game visual editor for UI (frames, text, images, buttons, inputs, scrollers, etc.)
- Block scripting for interactivity, logic, redirects, cookies, audio, tweens, etc.
- Claim unique domains (`.rbx`)
- Donation / purchase buttons (Robux)
- Milestone badges for visits + anniversary badges
- Collaboration (beta, up to 10 people)
- Discover other players’ sites
- Bookmark system
- Custom themes (Premium)
- Local system pages (`catweb://...`)
- Seasonal events (Halloween Hallway, egg hunts, candy, etc.)

Everything runs **client-side** inside the Roblox experience. There is no real web hosting or server-side code execution.

## How sites work

Sites are trees of positioned elements described in JSON.  
Players build them in the editor, then publish.  
JSON can be exported/imported — this is what AI agents generate.

## Key facts AIs should know when explaining CatWeb

- Not the real internet — pure Roblox simulation
- Landscape orientation focus
- Free tier is limited (element count, domains, etc.) — see `01-core/Limits.md`
- Scripts use **numeric variable names** and exact action IDs from the authoritative table
- Text filter exists; very long strings sometimes need the decoder pattern
- Community lives on Discord, in-game, Fandom wiki, and sites like `wiki.rbx` / `dotab.rbx`
- High-status signals: 10k Visits badge, well-known domains, useful tools

## Official / community resources

- Game: [CatWeb on Roblox](https://www.roblox.com/games/16855862021/CatWeb-Make-a-Website)
- In-game encyclopedia: `wiki.rbx`
- Fandom: https://catweb.fandom.com
- This repo (`catweb-guide`) — the AI-oriented knowledge base

## Short history notes

- Early 2024: public launch, rapid iteration
- Feb 2025: major script editor replacement
- Mar 2025: Anniversary Update (badges, many UI/scripting quality features)
- Late 2025: Collaboration beta, Hallway event, higher limits
- 2026: brief “Downage” (Roblox review, ~2 days)
