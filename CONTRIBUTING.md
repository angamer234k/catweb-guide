# Contributing to `cwukb`

Thanks for helping keep the ultimate CatWeb knowledge base accurate.

## What this repo is for

- **AI agents** that generate or reason about CatWeb sites
- Humans who need a single, trustworthy reference

Priority is always: correctness of the output contract and action shapes > extra fluff.

## How to contribute

1. Fork the repo
2. Make your changes on a branch
3. Open a PR with a clear description

### Especially welcome

- Confirmed new action IDs / parameter shapes after a game update
- Fixes to any rule that no longer matches the live game
- High-quality, importable example JSONs
- Better explanations of common failure modes

### Please avoid

- Inventing undocumented properties or action IDs
- Adding examples that would fail import/publish
- Large unrelated rewrites of SiteGPT V11 (that file is the authoritative source)

## Updating after a CatWeb game update

1. Check `catweb://whats-new` and the block palette in-game
2. Update `VERSION.md`
3. If action shapes or element properties changed, update:
   - `01-core/SiteGPT-V11.md` (or note the delta)
   - `01-core/JSONScript.md` / `UIGPT.md`
   - `02-ai-agent/SKILL.md` if the hard rules changed
4. Add a short note in `03-community/updates.md`

## Code / JSON style

- All example sites must be valid, importable CatWeb JSON
- Follow the output contract and numeric variable rule
- Prefer the design tokens and patterns from SiteGPT

Questions? Open an issue or ping in the CatWeb Discord.
