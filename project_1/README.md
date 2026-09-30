# 📄 Smart Resume Parser & Candidate Analyzer

**Elevate Labs Internship — Project No. 1**

An automated, intelligent Resume Parser and Applicant Tracking System (ATS) Analyzer built using **Python, PyMuPDF, python-docx, spaCy NLP, Pandas, and Streamlit**. 

This system extracts structured information (Contact Details, Categorized Technical Skills, Education, Work Experience) from unstructured PDF and DOCX resume files, computes ATS job match compatibility, and provides an interactive dashboard with data export options (CSV & JSON).

---

## 🎯 Key Features

- **Multi-Format Text Extraction:** Supports both `.pdf` (via PyMuPDF / pymupdf) and `.docx` (via python-docx) resume files.
- **Named Entity & Contact Recognition:** Uses spaCy (`en_core_web_sm`) entity extraction and regex patterns for Candidate Name, Email, Phone (+91 & International formats), LinkedIn, and GitHub profile links.
- **Categorized Skill Taxonomy Matching:** Identifies and classifies technical and soft skills across 9 categories (Programming Languages, Web & Frontend, Backend & Frameworks, Data Science & AI/ML, Databases, Cloud & DevOps, Tools & Platforms, Software Engineering Concepts, Soft Skills).
- **Education & Experience Extraction:** Parses degree titles, field of study, institutions, passing years, and computes estimated total years of experience.
- **ATS Compatibility Score Engine:** Matches candidate profiles against target job descriptions, displaying a match percentage, overlap skills, missing skills, and hiring recommendations.
- **Single & Batch Resume Processing:** Upload individual resumes or process entire candidate pools in batch with interactive candidate ranking leaderboards.
- **Data Export:** Export parsed resume records to structured JSON and tabular CSV files.
- **Automated PDF Report Generation:** Included 1-2 page PDF report (`Smart_Resume_Parser_Report.pdf`) compiled programmatically using ReportLab in accordance with internship submission guidelines.

---

## 📁 Repository Structure

```
project_1/
├── app.py                          # Main Streamlit web application
├── resume_parser.py                # Core ResumeParser engine class
├── skills_db.py                    # Skill taxonomy database & normalization
├── generate_test_resumes.py        # Generator for 5 test resumes (PDF & DOCX)
├── generate_report.py              # Generator for 2-page PDF Project Report
├── test_parser.py                  # Verification & test runner script
├── run_app.py                      # App launcher script
├── Smart_Resume_Parser_Report.pdf  # 2-Page Project Report (PDF)
├── parsed_resumes_sample.json      # Sample output JSON deliverable
├── requirements.txt                # Python package dependencies
├── README.md                       # Project documentation
└── test_resumes/                   # 5 Test Resumes (PDF & DOCX)
    ├── 1_Alex_Rivers_Data_Scientist.pdf
    ├── 2_Priya_Sharma_FullStack_Developer.pdf
    ├── 3_Marcus_Vance_DevOps_Architect.docx
    ├── 4_Sarah_Jenkins_Frontend_Engineer.pdf
    └── 5_Rahul_Verma_Python_Backend_Developer.docx
```

---

## 🚀 Quick Start & Installation

### 1. Install Dependencies
```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Generate Test Resumes & Deliverables (Optional)
```bash
python generate_test_resumes.py
python generate_report.py
python test_parser.py
```

### 3. Run the Streamlit Application
```bash
streamlit run app.py
# OR
python run_app.py
```

Open your web browser at `http://localhost:8501`.

---

## 📊 Sample Parsing & ATS Scoring Output

```json
{
  "filename": "1_Alex_Rivers_Data_Scientist.pdf",
  "name": "Alex Rivers",
  "email": "alex.rivers@email.com",
  "phone": "+1 (555) 234-5678",
  "links": {
    "LinkedIn": "linkedin.com/in/alex-rivers-data",
    "GitHub": "github.com/alexrivers"
  },
  "skills": {
    "total_skills_count": 23,
    "categorized_skills": {
      "Programming Languages": ["Python", "R", "SQL"],
      "Data Science & AI / ML": ["Machine Learning", "Deep Learning", "NLP", "spaCy", "PyTorch", "TensorFlow", "Pandas", "NumPy", "scikit-learn"],
      "Databases & Storage": ["PostgreSQL"],
      "Cloud & DevOps": ["Docker", "AWS"],
      "Tools & Platforms": ["Git", "Streamlit"]
    }
  },
  "experience": {
    "estimated_years": 6
  },
  "ats_match": {
    "ats_score": 90.9,
    "match_percentage": "90.9%",
    "recommendation": "Excellent Match! High candidate suitability for this position."
  }
}
```

---

## 📑 Deliverables Check

- [x] **Codebase:** Clean, modular Python modules (`resume_parser.py`, `skills_db.py`, `app.py`).
- [x] **UI Application:** Interactive Streamlit dashboard with tabs for Single Parser, Batch Parser, Analytics, and Documentation.
- [x] **5 Test Resumes:** PDF and DOCX resume samples included in `test_resumes/`.
- [x] **Output Files:** Sample output in `parsed_resumes_sample.json` and exportable CSVs/JSONs in the UI.
- [x] **Project Report:** 2-page PDF report `Smart_Resume_Parser_Report.pdf` adhering to internship guidelines.

---

## 👤 Author
Developed for Elevate Labs Internship Task — Project No. 1.
