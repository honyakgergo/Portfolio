# VTSZ customs classifier

**A self-hosted vision-language model replacing a manual customs-classification workflow for a client.**

A machine-parts client (Zoomlion) classified products into Hungarian customs codes by hand, using a consumer chatbot plus Excel and PDF uploads. It was slow, and it was unclear whether their contracts even allowed the data to go to an external API. Running the model locally removes that question.

- **Model:** Qwen2.5-VL 7B, quantised and served through Ollama on a consumer GPU. It reads product images from the PDF catalogue together with text fields from the spreadsheet.
- **Two scenarios per item:** one machine-specific classification and one based on material or function. A Streamlit review app lets a customs expert pick.
- **Key fix:** the first version gave the model ~480 candidate codes per item and accuracy was poor. Cutting that to the ~12 relevant codes fixed most of it. The search space was the problem, not the model.
- **Result:** the correct code is among the two proposed scenarios every time, and the model's first choice is correct 58% of the time.

**Stack:** Python · Qwen2.5-VL · Ollama · Streamlit
