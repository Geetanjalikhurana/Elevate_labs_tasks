"""
test_parser.py
Quick test script for resume_parser.py
"""

import os
import json
from resume_parser import ResumeParser

def test_parsing():
    parser = ResumeParser()
    resumes_dir = "test_resumes"
    files = os.listdir(resumes_dir)
    print(f"Found {len(files)} test resumes.")
    
    sample_jd = """
    We are looking for a Senior Data Scientist / Machine Learning Engineer with experience in Python, PyTorch, TensorFlow, NLP, spaCy, Docker, PostgreSQL, SQL, and AWS. Candidate should have a Master's or Bachelor's degree in Computer Science or related field with strong communication and problem-solving skills.
    """

    results = []
    for fname in files:
        fpath = os.path.join(resumes_dir, fname)
        parsed = parser.parse(fpath, fname)
        ats_info = parser.calculate_ats_score(parsed, sample_jd)
        parsed["ats_match"] = ats_info
        results.append(parsed)
        
        print("="*60)
        print(f"File: {fname}")
        print(f"Candidate Name: {parsed['name']}")
        print(f"Email: {parsed['email']} | Phone: {parsed['phone']}")
        print(f"LinkedIn: {parsed['links']['LinkedIn']} | GitHub: {parsed['links']['GitHub']}")
        print(f"Total Skills Extracted: {parsed['skills']['total_skills_count']}")
        print(f"Categorized Skills: {list(parsed['skills']['categorized_skills'].keys())}")
        print(f"ATS Match Score: {ats_info['ats_score']}% ({ats_info['recommendation']})")

    # Save output files to root directory as required by deliverables
    with open("parsed_resumes_sample.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nSaved output sample to parsed_resumes_sample.json")

if __name__ == "__main__":
    test_parsing()
