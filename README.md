# Gergő Honyák — Project Portfolio

Third-year Applied Data Science & AI student at Breda University of Applied Sciences, starting a Data Science & AI pre-master at TU/e in September. I like finding patterns in data and building the whole thing around them — not just training a model, but the pipeline, the app, and the honest evaluation that tells you whether it actually works.

Most of my recent work points at **quantitative finance**: strategy research, backtesting, risk, and live market tooling. Alongside that I've built computer-vision, NLP, and MLOps projects across my degree. This repo collects the ones I'm happy to be judged on.

---

## Featured projects

### [SwingLab](swinglab)
A research platform, backtester, and live monitor, and MOM_BROAD, the weekly cross-sectional momentum strategy it runs with real capital since February 2026: a 34.7% CAGR at a 1.27 Sharpe backtested daily since 2016, and a 1.59 Sharpe live so far. FastAPI + React, with a full stress-test suite (walk-forward, crisis periods, block-bootstrap Monte Carlo, parameter sensitivity).

<p align="center"><img src="swinglab/images/equity_curve.png" width="75%" alt="SwingLab equity curve" /></p>

### [Graph Neural Networks for Stock Prediction](GNN%20project)
My first quant project: can a GNN predict quarterly Nasdaq-100 returns by modelling the correlation graph between stocks? Statistically significant predictive power (IC 0.051, t = 2.77, p = 0.007) over an 83-quarter walk-forward, and a 9.48% annualised alpha against QQQ (t = 2.80, p = 0.005).

<p align="center"><img src="GNN%20project/visuals/cumulative.png" width="75%" alt="GNN cumulative returns" /></p>

### [Sentify — Emotion-Classification MLOps Pipeline](sentify-emotion-pipeline)
A team, production-style MLOps system for Banijay Benelux: video/audio → transcript with per-sentence emotion. Fine-tuned BERT (F1 0.41 → 0.84 with focal loss), served from a Docker Compose stack (FastAPI · React · Streamlit · MLflow · Postgres · MinIO) with Azure ML training and an Airflow retraining loop.

<p align="center"><img src="sentify-emotion-pipeline/images/xai_gui.png" width="75%" alt="Sentify prediction interface" /></p>

### [proper_validation — Adversarial Backtest Validator](proper-validation)
A tool that attacks a backtest you've already run and reports how much of the claimed edge survives: deflated Sharpe against a simulated best-of-N null, probability of backtest overfitting, Fama-French 5 + momentum attribution, cost fragility, survivorship counted against real index membership, and a behavioural look-ahead test that re-runs the strategy on corrupted futures. Statistical and engine verdicts are kept separate. It detects 96% of the planted defects in the labelled benchmarks with 0% false positives on the one real edge, and ships as a CLI plus a Claude Code skill. ([repo](https://github.com/honyakgergo/proper-validation))

<p align="center"><img src="proper-validation/images/haircut_cascade.png" width="75%" alt="Sharpe ratio after each honest adjustment" /></p>

### [money_dashboard](money-dashboard)
A live market-analytics terminal, and the screen I actually read every day — sector breadth and rotation (RRG vs SPY), the full volatility complex (term structure, VVIX, SKEW, variance risk premium, dispersion), macro & regime (yfinance + FRED), commodities and roll yield, weekly positioning (CFTC asset-manager and leveraged-fund net, NAAIM, AAII), and per-name research with fundamentals, earnings, analyst opinion and the option surface next to the price chart. Ten pages driven by a market-session clock.
<p align="center"><img src="money-dashboard/images/cross-asset-rrg.png" width="75%" alt="money_dashboard Cross-Asset page — Relative Rotation Graph and correlation matrix" /></p>

### [NPEC — Root Analysis, Robotics & Inpainting Research](npec-root-analysis)
Two connected pieces of work with the Netherlands Plant Eco-phenotyping Centre: an end-to-end pipeline (U-Net segmentation → skeletonize → Dijkstra → sub-millimetre PID/RL robot inoculation) and a research study on repairing gaps in root masks (BCE U-Net winner, validated with Wilcoxon tests at p < 0.001 across 9,014 patches).

<p align="center"><img src="npec-root-analysis/images/pid_controller.gif" width="60%" alt="PID-controlled robot arm" /></p>

### [Clash Analyzer](clash-analyzer)
A Clash Royale progress tracker and battle-analytics dashboard on the official API. The API only remembers the last ~30 games, so a background poller stores every battle and profile snapshot. From that history it computes tilt detection, session fatigue, levels vs skill, nemesis cards, an upgrade planner, and a comparison against a daily crawl of the top-100 meta. Every rate comes with a Wilson interval. FastAPI + SQLite backend, React 19 + TypeScript frontend. ([repo](https://github.com/honyakgergo/clash-analyzer))

<p align="center"><img src="clash-analyzer/images/overview.png" width="75%" alt="Clash Analyzer player overview" /></p>

### [Waste Warrior](waste-warrior)
A deep-learning waste classifier wrapped in a full Flask app: MobileNet transfer learning to 97.7% accuracy, with Grad-CAM / LIME / integrated-gradients explainability to confirm the model looks at the object, not the background.

<p align="center"><img src="waste-warrior/images/output_1.png" width="45%" alt="Waste classifier prediction" /></p>
<p align="center"><img src="waste-warrior/images/output_2.png" width="45%" alt="Waste classifier prediction" /></p>

---

## More projects

- **[VTSZ customs classifier](vtsz-customs-classifier):** a self-hosted vision-language model (Qwen2.5-VL on Ollama) that replaces a manual Excel and PDF customs-classification workflow for a client.
- **[IMC Prosperity 4](imc-prosperity-4):** a global algorithmic trading competition, 223rd of ~18,800 teams solo and 1st in the Netherlands on the manual round.
- **[Receipt extraction](receipt-extraction):** Tesseract OCR plus a Llama model that turns messy scanned receipts into clean structured data.
- **[AI Engineer internship](ai-engineer-internship):** a production RAG system with a custom LLaMA model and an interactive avatar, deployed on GCP.

---

## What I work with

**Languages** — Python, SQL, JavaScript

**ML / DL** — PyTorch, TensorFlow/Keras, scikit-learn, Transformers, PyTorch Geometric

**Quant** — pandas, NumPy, SciPy, yfinance, backtesting & stress-testing, Robert Carver-style systematic design

**MLOps / Infra** — FastAPI, Docker, MLflow, Airflow, Postgres, Azure ML, GitHub Actions

**Frontend** — React, Vite

## A bit more

I got into quant after reading Marcos López de Prado's *Advances in Financial Machine Learning*, and I've since competed solo in **IMC Prosperity 4** (223rd of ~18,800 teams; 1st in the Netherlands on the manual round). I'm open to quant research / trading and data science internships in Amsterdam.

Each project folder has its own detailed README with figures. Have a look around.
