import streamlit as st
import tempfile
from extract_text import extract_from_pdf, extract_from_docx
from ai_analysis import analyze_resume, generate_cover_letter

st.set_page_config(page_title="AI Resume Assistant", page_icon="📄")
st.title("📄 AI Resume & Job Match Assistant (Gemini 1.5)")

uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])
job_desc = st.text_area("Paste Job Description here:")

if uploaded_file and job_desc:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    if uploaded_file.name.endswith(".pdf"):
        resume_text = extract_from_pdf(tmp_path)
    else:
        resume_text = extract_from_docx(tmp_path)

    if st.button("🔍 Analyze Resume"):
        st.subheader("AI Analysis")
        with st.spinner("Analyzing resume..."):
            result = analyze_resume(resume_text, job_desc)
        st.write(result)

    if st.button("✉️ Generate Cover Letter"):
        st.subheader("Tailored Cover Letter")
        with st.spinner("Generating cover letter..."):
            letter = generate_cover_letter(resume_text, job_desc)
        st.write(letter)
        st.download_button("Download Cover Letter", letter, file_name="cover_letter.txt")
