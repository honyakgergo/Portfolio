# Gergő Honyák · Project Portfolio

Data Science & AI pre-master student at TU/e, with a BSc background in Applied Data Science & AI from Breda University of Applied Sciences. Most of my recent work is quantitative finance: strategy research, backtest validation and a momentum strategy I trade with real money. Before that I built computer vision, NLP and MLOps projects, and spent a year as an AI engineer intern.

Each folder has a short write-up with figures. Certified as an Associate Data Scientist by DataCamp ([certificate](certifications)).

## Quant

| Project | What it is | Key result |
|---|---|---|
| [MOM_BROAD](swinglab) | Weekly cross-sectional momentum strategy on ~515 US large caps, trading live capital | Backtest 2016 to 2026: 34.7% CAGR, 1.27 Sharpe. Live since Feb 2026: +51.8%, 1.59 Sharpe |
| [proper_validation](proper-validation) | Adversarial validator for finished backtests: deflated Sharpe, PBO, factor attribution, behavioural look-ahead test | Catches 96% of planted defects, 0% false positives on the real edge |
| [IMC Prosperity 4](imc-prosperity-4) | Global algorithmic trading competition, solo | 223rd of ~18,800 teams, 1st in the Netherlands on the manual rounds |
| [GNN stock prediction](GNN%20project) | Graph neural network on a Nasdaq-100 correlation graph, 83-quarter walk-forward | IC 0.051 (t = 2.77), but no significant edge over a plain momentum baseline |
| [money_dashboard](money-dashboard) | Daily market-monitoring terminal: breadth, rotation, volatility, positioning | Ten pages, used every trading day |

## Machine learning and engineering

| Project | What it is | Key result |
|---|---|---|
| [AI Engineer internship](ai-engineer-internship) | Production RAG assistant on a self-hosted Llama model, deployed on GCP | Jun 2025 to Jun 2026, live to real users |
| [Sentify](sentify-emotion-pipeline) | Team MLOps project for Banijay: video to per-sentence emotion, with automated retraining | Macro F1 0.41 to 0.84 after fixing a confidence collapse |
| [NPEC root analysis](npec-root-analysis) | U-Net root segmentation, root-length measurement, robot control, and a gap-inpainting study | Sub-millimetre robot positioning; BCE U-Net best at p < 0.001 |
| [VTSZ customs classifier](vtsz-customs-classifier) | Self-hosted vision-language model for customs-code classification, for a client | Candidate list cut from ~480 to ~12 codes; 58% top-1 |
| [Waste Warrior](waste-warrior) | Waste image classifier in a Flask app, with explainability | 97.7% test accuracy (MobileNet transfer learning) |
| [Clash Analyzer](clash-analyzer) | Side project: battle analytics on the Clash Royale API | Wilson interval on every rate, 112 tests |

## Stack

- **Languages:** Python, SQL, JavaScript / TypeScript
- **ML:** PyTorch, PyTorch Geometric, TensorFlow / Keras, scikit-learn, Transformers
- **Quant:** pandas, NumPy, SciPy, statsmodels, walk-forward and Monte Carlo testing
- **MLOps:** FastAPI, Docker, MLflow, Airflow, Postgres, Azure ML, GCP Cloud Run, GitHub Actions
