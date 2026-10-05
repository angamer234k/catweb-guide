# What is CatWeb? (Overview for AIs & Humans)

**CatWeb** is a Roblox game created by **HumanCat222** (@CcXxiiHuman_C4t) where players build fully functional 2D websites inside a browser simulation.

- **TLD:** `.rbx` (exclusive to the game — not a real internet domain)
- **Inspiration:** Google Chrome (explicit parody — “Do not take it seriously”)
- **Public release:** March 2024 (Anniversary: March 24)
- **Development start:** April 2024
- **Scripting:** Visual block-based language (similar to Scratch), stored/shared as special JSON
- **~730k sites** registered (community estimate from wiki.rbx)

## Core features

- In-game visual editor for UI (frames, text, images, buttons, inputs, scrollers, etc.)
- Block scripting for interactivity, logic, redirects, cookies, audio, tweens, etc.
- Claim unique domains (`.rbx`)
- Donation / purchase buttons (Robux)
- Milestone badges for visits
- Collaboration (beta)
- Discover other players’ sites
- Bookmark system
- Custom themes (Premium)
- Local system pages (`catweb://...`)

Everything runs **client-side** inside the Roblox experience. There is no real web hosting or server-side code.

## How sites work

Sites are trees of positioned elements described in JSON.  
Players build them in the editor, then publish.  
JSON can be exported/imported (this is what AI agents generate).

## Key facts AIs should know when explaining CatWeb

- Not the real internet — pure Roblox simulation
- Landscape only
- Free tier is limited (100 elements, 1 free domain, etc.) — see `01-core/Limits.md`
- Scripts use numeric variable names and exact action IDs
- Filter exists on text; long strings sometimes need the decoder
- Community is active on Discord + in-game + Fandom wiki

## Official / community resources

- Game: [CatWeb on Roblox](https://www.roblox.com/games/16855862021/CatWeb-Make-a-Website)
- In-game wiki-style site: `wiki.rbx`
- Fandom: https://catweb.fandom.com
- This repo (`catweb-guide`) — the AI-oriented knowledge base
