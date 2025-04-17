# 🖼️ AI-Based Image Caption Generator

A GenAI-powered web app that generates **engaging, creative Instagram-style captions** and hashtags based on uploaded images or text descriptions.

---

## 🚀 Features

- 📸 Upload an image and get 5 unique, stylized captions
- ✍️ Or enter a manual description to generate captions
- 🎯 Automatically suggests 10 relevant Instagram hashtags
- ⚙️ Powered by **Mistral** via **Ollama** (runs locally, no API keys!)
- 💻 Simple UI built using **Streamlit**
- 🔎 Uses BLIP (vision-language model) for image captioning

---


---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
 -- git clone https://github.com/arun4589/AI-Caption-Generator.git
 -- cd AI-Caption-Generator
```

### 2. Activate the environment
 -- python -m venv caption

# On Windows:
caption\Scripts\activate
# On Mac/Linux:
source caption/bin/activate
### 3.necessary installations
pip install -r requirements.txt
ollama pull mistral
ollama run mistral
streamlit run app.py




