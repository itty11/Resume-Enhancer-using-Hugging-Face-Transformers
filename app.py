import gradio as gr
import PyPDF2
from transformers import pipeline

# ---------- Load Hugging Face Models ----------
# We'll use FLAN-T5 for enhancement and summarization
enhancer = pipeline("text2text-generation", model="google/flan-t5-large", max_length=1024)
keyword_extractor = pipeline("text2text-generation", model="google/flan-t5-base")

# ---------- Utility Functions ----------
def extract_text_from_pdf(pdf_file):
    """Extract text content from a PDF file."""
    text = ""
    try:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        for page in pdf_reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    except Exception as e:
        text = f"Error reading PDF: {e}"
    return text.strip()

def split_text(text, max_length=512):
    """Split long text into smaller chunks for model processing."""
    words = text.split()
    chunks = []
    current = []

    for word in words:
        current.append(word)
        if len(current) >= max_length:
            chunks.append(" ".join(current))
            current = []
    if current:
        chunks.append(" ".join(current))
    return chunks

# ---------- AI Resume Enhancer ----------
def enhance_resume(pdf_file, job_description):
    if not pdf_file:
        return "⚠️ Please upload a PDF file."
    if not job_description:
        return "⚠️ Please provide a job description."

    resume_text = extract_text_from_pdf(pdf_file)
    if not resume_text:
        return "⚠️ Could not extract text from the uploaded PDF."

    # Step 1: Extract job title from job description
    job_title_prompt = f"Extract the main job title from this description:\n\n{job_description}"
    job_title = keyword_extractor(job_title_prompt, max_length=30)[0]['generated_text']

    # Step 2: Extract top ATS keywords from job description
    keyword_prompt = f"Extract 10 important ATS keywords from this job description:\n\n{job_description}"
    ats_keywords = keyword_extractor(keyword_prompt, max_length=80)[0]['generated_text']

    # Step 3: Split resume text to handle long content
    chunks = split_text(resume_text, max_length=400)
    enhanced_chunks = []

    for chunk in chunks:
        prompt = f"""
        You are an expert AI Resume Writer.
        Enhance the following resume section to make it more professional, concise,
        and aligned with the job title "{job_title}".
        Also ensure it includes relevant ATS keywords such as: {ats_keywords}.
        Improve tone, grammar, and job relevance.

        Resume Section:
        {chunk}

        Enhanced Section:
        """
        result = enhancer(prompt, max_length=512, do_sample=True)[0]['generated_text']
        enhanced_chunks.append(result)

    enhanced_resume = "\n".join(enhanced_chunks)

    return f"""
🧠 **Detected Job Title:** {job_title}

🔑 **Recommended ATS Keywords:** {ats_keywords}

📄 **Enhanced Resume:**
{enhanced_resume}
"""

# ---------- Gradio Interface ----------
app = gr.Interface(
    fn=enhance_resume,
    inputs=[
        gr.File(label="Upload Resume (PDF)", file_types=[".pdf"]),
        gr.Textbox(label="Paste Job Description", lines=8, placeholder="Enter job description here...")
    ],
    outputs=gr.Textbox(label="Enhanced Resume Output", lines=25),
    title="🚀 AI Resume Enhancer with Job Title Extraction & ATS Optimization",
    description=(
        "Upload your resume and job description. "
        "This AI tool extracts the job title, optimizes your resume with relevant ATS keywords, "
        "and enhances professionalism, tone, and job relevance using Hugging Face Transformers."
    )
)

if __name__ == "__main__":
    app.launch()
