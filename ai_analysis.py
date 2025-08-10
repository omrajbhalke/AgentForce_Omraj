import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def analyze_resume(resume_text, job_description):
    prompt = f"""
    You are a professional career coach.
    Compare the following resume with the job description.
    Identify:
    1. Missing keywords or skills.
    2. Suggestions for improvement in structure and content.
    3. Rating (0-100) on job match.

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

def generate_cover_letter(resume_text, job_description):
    prompt = f"""
    You are an expert career advisor.
    Using the resume content and job description below, create a concise and 
    professional cover letter tailored for the specific role.
    The cover letter should be:
    - 3-4 short paragraphs
    - Professional tone
    - Highlight the most relevant skills and experiences
    - End with a call to action

    Resume:
    {resume_text}

    Job Description:
    {job_description}
    """
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
