# AI Engineer internship · AIGENTIC Compliance

**Jun 2025 to Jun 2026. A production RAG assistant on a self-hosted Llama model, deployed on Google Cloud.**

## What I built

- **Model serving.** A Llama 3 model containerised and deployed on GCP Cloud Run, tuned for low response latency. The container scales to zero during night hours, which cuts cloud cost when nobody is using it.
- **RAG pipeline.** Retrieval over company documents, so answers are grounded in the source material rather than the model's memory.
- **Proxy API.** A proxy layer between the frontend, the model and the external APIs, built with a senior engineer and slotted into the existing infrastructure.
- **CI/CD.** An automated pipeline that runs tests and linting on every change before building and deploying.
- **Usage dashboard.** A monitoring dashboard on GCP that queries the stored user data: interactions, API calls and performance across the website and the app.
- **Frontend.** A FastAPI backend with a JavaScript frontend and an interactive avatar interface, plus a small Unity demo of the product.

**Stack:** Python · FastAPI · Llama · GCP Cloud Run · Firebase · Docker · CI/CD · JavaScript
