# 🚀 AI Resume Enhancer using Hugging Face Transformers

An **AI-powered Resume Enhancer** built using **Hugging Face Transformers**, **Gradio**, and **LangChain**.  
This app analyzes your resume, enhances its language and clarity, optimizes for **ATS (Applicant Tracking Systems)**, and aligns your profile with the **job description** automatically.

---

## ✨ Features

✅ Upload your Resume (PDF format)  
✅ AI-based professional rewriting using **FLAN-T5 Large**  
✅ **Automatic Job Title Extraction** from job description  
✅ **ATS Keyword Optimization** for better recruiter visibility  
✅ Unlimited text support (automatic chunk splitting)  
✅ Simple and elegant **Gradio Web UI**  
✅ Deployable on **Hugging Face Spaces** or **GitHub Pages**

---

## 🧩 Tech Stack

- **Python 3.10+**
- **Transformers (Hugging Face)**
- **LangChain**
- **Gradio**
- **PyPDF2**

---

## 🛠️ Installation & Run (Local)

1️⃣ Clone the repository:

git clone https://github.com/<your-username>/ai-resume-enhancer.git

cd ai-resume-enhancer

2️⃣ Create a virtual environment and activate it:

python -m venv venv

venv\Scripts\activate    # Windows

source venv/bin/activate # macOS/Linux

3️⃣ Install dependencies:

pip install -r requirements.txt

4️⃣ Run the app:

python app.py

5️⃣ Open your browser at:

http://127.0.0.1:7860

## Usage

1. Upload your resume (PDF)

2. Paste the job description

3. The AI:

  Extracts resume text
  
  Enhances tone & clarity
  
  Optimizes with job-related keywords
  
  Suggests improvements aligned to the job title

## ☁️ Deployment on Hugging Face Spaces

1. Go to: https://huggingface.co/spaces

2. Click “New Space”

3. Set:

  Space name: resume-enhancer-ai
  
  SDK: Gradio
  
  Visibility: Public

4. Upload these files:

  app.py
  
  requirements.txt
  
  README.md

5. Click Commit changes

The app will build automatically and go live at:

👉 https://huggingface.co/spaces/ittyavira/resume-enhancer-ai

## 🤖 Future Enhancements

1. Resume scoring system

2. Multi-language support

3. AI-based cover letter generation

4. Export enhanced resume to PDF or DOCX

---
title: Resume Enhancer Ai
emoji: 😻
colorFrom: blue
colorTo: blue
sdk: gradio
sdk_version: 5.49.1
app_file: app.py
pinned: false
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference

## 👨‍💻 Author

Ittyavira C Abraham

MCA (AI) @ Amrita Vishwa Vidyapeetham (Amrita Ahead)

💡 Passionate about AI, ML, NLP, and Intelligent Systems
