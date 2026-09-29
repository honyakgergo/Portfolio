# VTSZ customs classifier

**A local vision-language model replaces a manual Excel and PDF customs-classification workflow.**

Client · Solo · Applied vision-language · 2025 · Working prototype

| Candidate recall | Final pick split | Candidate list, pruned |
|---|---|---|
| **100%** | **58/42** | **480 → 12** |

---

A client (Zoomlion machine parts) was manually classifying products into Hungarian customs codes using a consumer chat tool plus Excel and PDF uploads, slow, and it wasn't even clear whether the client's contracts allowed external APIs to touch this data. This project builds a self-hosted alternative that sidesteps that question entirely.

A local Qwen2.5-VL 7B model, quantized and served through Ollama on a consumer GPU, reads product images pulled from the PDF catalog alongside text fields from the source spreadsheet. For each item it proposes two competing classification scenarios, one machine-specific, one material or function based, and a Streamlit review app lets a customs expert pick between them.

The first version fed the model a candidate list of roughly 480 possible codes per item, and accuracy was bad. Narrowing that list down to the roughly 12 actually relevant codes per item fixed nearly all of it, the model was never the real constraint, the search space was. The model now retrieves the right pair of candidates 100% of the time and picks the correct final code 58% of the time, with its own confidence signal well-calibrated against human corrections, a lead for improving accuracy without retraining anything.

**Stack:** `Python` · `Qwen2.5-VL` · `Ollama` · `Streamlit`
