import re
import pdfplumber
from docx import Document


SKILLS = [
    "python",
    "django",
    "sql",
    "html",
    "css",
    "javascript",
    "rest api",
    "git",
    "aws"
]

JOB_SKILLS = [
    "python",
    "django",
    "sql",
    "git",
    "aws"
]

def extract_text(file_path):

    text = ""

    if file_path.endswith(".pdf"):

        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif file_path.endswith(".docx"):

        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    return text.lower()


def extract_email(text):

    email = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return email.group() if email else ""


def extract_phone(text):

    phone = re.search(
        r"\+?\d[\d\s-]{8,15}",
        text
    )

    return phone.group() if phone else ""


def extract_skills(text):

    found_skills = []

    for skill in SKILLS:

        if skill.lower() in text:
            found_skills.append(skill)

    return found_skills



def calculate_score(candidate_skills):

    matched = len(
        set(candidate_skills)
        & set(JOB_SKILLS)
    )

    score = round(
        (matched / len(JOB_SKILLS)) * 100
    )

    return score


def extract_education(text):

    education_keywords = [
        "b.tech",
        "btech",
        "bachelor of technology"
    ]

    for keyword in education_keywords:
        if keyword in text.lower():
            return "B.Tech"

    return "Not Found"

def get_resume_status(score):

    if score >= 80:
        return "Excellent Match"

    elif score >= 60:
        return "Good Match"

    return "Needs Improvement"