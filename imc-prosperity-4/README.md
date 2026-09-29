# IMC Prosperity 4

**A global algorithmic trading competition, entered solo: 223rd of ~18,800 teams, 7th in the Netherlands, and 1st in the Netherlands (33rd globally) on the manual rounds.**

<p align="center"><img src="images/leaderboard.jpg" width="85%" alt="Final leaderboard: #223 overall, #7 country, #33 manual globally" /></p>

Each round combined an algorithmic trading challenge with a separate manual puzzle, against more than 30,000 participants.

- **Options:** priced the voucher options, fitted implied volatility to a smile across strikes, and traded deviations from the smile as cross-sectional z-scores.
- **Market making:** quoted around fair value while managing inventory, with a regime layer adjusting to shifts in the simulated market.
- **Round 3 lesson:** an algorithm that looked excellent on the backtest fell apart on live data. From then on I chose strategies that made theoretical sense over ones that scored best on history, which drove rounds 4 and 5.
- **Manual rounds:** I assumed most players would paste the puzzle into an LLM and take the first answer, so I modelled where the crowd would cluster and positioned against it.

**Stack:** Python · NumPy · pandas
