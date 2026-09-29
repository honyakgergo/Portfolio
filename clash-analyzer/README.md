# Clash Analyzer

**A side project: progress tracking and battle analytics on the official Clash Royale API.** Code and setup: [github.com/honyakgergo/clash-analyzer](https://github.com/honyakgergo/clash-analyzer)

The API only remembers the last ~30 battles, so a background poller stores every battle and profile snapshot in SQLite and history builds up over time. **Every rate carries a 95% Wilson interval, and an insight only appears once the sample can support it.**

<p align="center"><img src="images/battles.png" width="85%" alt="Battle analytics: tilt, session fatigue, levels vs skill, nemesis cards" /></p>

- **Battle analytics:** tilt (win rate after wins and losses), session fatigue, levels against skill, elixir leaked, nemesis cards, best time to play.
- **Upgrade planner:** gold and card copies needed per level, from a hand-maintained cost table checked in tests.
- **Meta comparison:** a daily crawl of the top 100 players gives card win rates and top decks to compare your deck against.

**Stack:** Python 3.12 · FastAPI · SQLModel / SQLite · APScheduler · React 19 · TypeScript · Tailwind · pytest (112 tests, 95% coverage)

Not affiliated with or endorsed by Supercell.
