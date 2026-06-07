# Resume Analyzer

A Resume Analyzer built using Django REST Framework that extracts candidate information from PDF resumes.

## Features

* Upload PDF Resume
* Extract Email Address
* Extract Phone Number
* Extract Skills
* Extract Education (B.Tech)
* Calculate Resume Match Score
* Resume Status Evaluation
* REST API Integration
* Bootstrap Frontend

## Tech Stack

* Python
* Django
* Django REST Framework
* HTML
* CSS
* Bootstrap
* JavaScript
* PDFPlumber
* SQLite

## Project Structure

resume_analyzer/

├── analyser/

├── config/

├── static/

├── templates/

├── requirements.txt

├── README.md

└── manage.py

## Sample API Response

{
"email": "[example@gmail.com](mailto:example@gmail.com)",
"phone": "+91 9876543210",
"education": "B.Tech",
"skills": [
"python",
"django",
"sql"
],
"score": 80,
"status": "Excellent Match"
}

## Future Enhancements

* ATS Resume Matching
* Job Description Matching
* User Authentication
* Resume History
* PDF Report Download
