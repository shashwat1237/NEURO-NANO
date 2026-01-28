# 🧠 NEURO-NANO

**Neuro-Nano** is a lightweight local AI inference setup using a quantized GGUF model, designed for fast execution, offline usage, and low-resource systems.

This repository contains the **inference code and runtime tools**.
The **model weights are hosted separately** on Hugging Face.

---

## 🚀 Features

* ⚡ Fast local inference
* 🧠 GGUF-based LLM support
* 💻 Runs fully offline
* 🪶 Optimized for low-RAM systems
* 🧩 Modular and extensible

---

## 📦 Model Weights

Due to GitHub file size limits, the model is hosted on Hugging Face.

🔗 **Download Model:**
[https://huggingface.co/FREAKKAERF/neuro-nano](https://huggingface.co/FREAKKAERF/neuro-nano)

---

## 📁 Project Structure

```
NEURO-NANO/
│
├── tools/                 # LLaMA / GGML runtime binaries
├── scripts/               # Run & inference scripts
├── SYSTEM_PROMPT.txt      # System prompt config
├── project_documentation.pdf
├── manual.pdf
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/shashwat1237/NEURO-NANO.git
cd NEURO-NANO
```

---

### 2️⃣ Download the model

Download `nano.gguf` from:

👉 [https://huggingface.co/FREAKKAERF/neuro-nano](https://huggingface.co/FREAKKAERF/neuro-nano)

Place it inside:

```
NEURO-NANO/
```

---

### 3️⃣ Run the model

#### Windows

```bash
scripts\run_chat.bat
```

#### Linux / Mac

```bash
bash scripts/run_chat.sh
```

---

## 🧠 Example (Python Auto-Download)

```python
from huggingface_hub import hf_hub_download

model_path = hf_hub_download(
    repo_id="FREAKKAERF/neuro-nano",
    filename="nano.gguf"
)
```

---

## 🛠 Requirements

* Windows / Linux
* Python 3.10+
* Git
* 8GB+ RAM recommended

---

## 📌 Notes

* Model files are **not stored in this repo**
* Uses **Git LFS on Hugging Face**
* Designed for **local inference**
* Optimized for hackathon demos

---

## 📜 License

MIT License

---

## 👨‍💻 Author

**Shashwat**
GitHub: [https://github.com/shashwat1237](https://github.com/shashwat1237)
Model: [https://huggingface.co/FREAKKAERF/neuro-nano](https://huggingface.co/FREAKKAERF/neuro-nano)
 
