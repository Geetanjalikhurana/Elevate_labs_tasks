"""
app.py
Streamlit Web Application for Smart Resume Parser (Elevate Labs Task - Project No. 1)
"""

import streamlit as st
import pandas as pd
import json
import os
import io
from resume_parser import ResumeParser
from generate_report import create_project_report

# Page Config
st.set_page_config(
    page_title="Smart Resume Parser",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.2rem;
        color: #1E3A8A;
        font-weight: 700;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1.05rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .metric-card {
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        border-radius: 10px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #2563EB;
    }
    .metric-label {
        font-size: 0.85rem;
        color: #64748B;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .skill-badge {
        display: inline-block;
        background-color: #EFF6FF;
        color: #1E40AF;
        border: 1px solid #BFDBFE;
        border-radius: 15px;
        padding: 4px 12px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 3px;
    }
    .section-card {
        background-color: #FFFFFF;
        border: 1px solid #E2E8F0;
        border-radius: 8px;
        padding: 18px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)


@st.cache_resource
def get_parser():
    return ResumeParser()

parser = get_parser()

# Title Header
st.markdown('<div class="main-header">📄 Smart Resume Parser & Candidate Analyzer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Automated extraction of Skills, Education, Experience & ATS Match Scoring from PDF/DOCX resumes</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://img.icons8.com/isometric-folders/100/resume.png", width=70)
st.sidebar.title("Smart Parser Controls")
st.sidebar.markdown("---")

# Sample Resumes Directory check
SAMPLE_DIR = "test_resumes"
if not os.path.exists(SAMPLE_DIR):
    from generate_test_resumes import generate_all_resumes
    generate_all_resumes()

sample_files = [f for f in os.listdir(SAMPLE_DIR) if f.endswith(('.pdf', '.docx'))] if os.path.exists(SAMPLE_DIR) else []

st.sidebar.subheader("Quick Actions")
if st.sidebar.button("⚡ Load 5 Sample Test Resumes", use_container_width=True):
    st.session_state["load_samples"] = True

st.sidebar.markdown("---")
st.sidebar.subheader("Project Documentation")
# Check/Generate Report
report_pdf_path = "Smart_Resume_Parser_Report.pdf"
if not os.path.exists(report_pdf_path):
    create_project_report(report_pdf_path)

with open(report_pdf_path, "rb") as f:
    pdf_bytes = f.read()

st.sidebar.download_button(
    label="📥 Download Project Report (PDF)",
    data=pdf_bytes,
    file_name="Smart_Resume_Parser_Report.pdf",
    mime="application/pdf",
    use_container_width=True
)

st.sidebar.info("💡 **Project Guidelines Met:**\n- PDF/DOCX Parsing\n- spaCy + Regex Skill Extraction\n- JSON & CSV Export\n- ATS Matching Engine\n- 2-Page PDF Report")

# Main Navigation Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "👤 Single Resume Parser", 
    "👥 Batch Resume Parser & Ranking", 
    "📊 Skill Analytics", 
    "📑 Project Report & Specs"
])

# ---------------------------------------------------------
# TAB 1: SINGLE RESUME PARSER
# ---------------------------------------------------------
with tab1:
    st.subheader("Parse Single Resume & Calculate ATS Score")
    
    col_up, col_sample = st.columns([2, 1])
    with col_up:
        uploaded_file = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"], key="single_uploader")
    with col_sample:
        selected_sample = st.selectbox("Or Choose a Test Resume:", ["None"] + sample_files)

    file_to_parse = None
    filename = "resume.pdf"

    if uploaded_file is not None:
        file_to_parse = uploaded_file
        filename = uploaded_file.name
    elif selected_sample != "None":
        sample_path = os.path.join(SAMPLE_DIR, selected_sample)
        with open(sample_path, "rb") as f:
            file_to_parse = io.BytesIO(f.read())
        filename = selected_sample

    if file_to_parse is not None:
        with st.spinner("Extracting text and analyzing candidate profile..."):
            parsed_data = parser.parse(file_to_parse, filename)

        st.success(f"Successfully Parsed: **{filename}**")

        # Top Summary Metrics
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{parsed_data["name"]}</div><div class="metric-label">Candidate Name</div></div>', unsafe_allow_html=True)
        with m2:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{parsed_data["skills"]["total_skills_count"]}</div><div class="metric-label">Skills Found</div></div>', unsafe_allow_html=True)
        with m3:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{parsed_data["experience"]["estimated_years"]} yrs</div><div class="metric-label">Est. Experience</div></div>', unsafe_allow_html=True)
        with m4:
            st.markdown(f'<div class="metric-card"><div class="metric-value">{len(parsed_data["education"])}</div><div class="metric-label">Edu Entries</div></div>', unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Contact Details Card
        c1, c2 = st.columns(2)
        with c1:
            st.markdown("### 📇 Contact Information")
            st.markdown(f"- **Email:** `{parsed_data['email']}`")
            st.markdown(f"- **Phone:** `{parsed_data['phone']}`")
            st.markdown(f"- **LinkedIn:** [{parsed_data['links']['LinkedIn']}]({parsed_data['links']['LinkedIn']})")
            st.markdown(f"- **GitHub:** [{parsed_data['links']['GitHub']}]({parsed_data['links']['GitHub']})")

        with c2:
            st.markdown("### 🎓 Education & Background")
            if parsed_data["education"]:
                for item in parsed_data["education"]:
                    st.markdown(f"- {item}")
            else:
                st.info("No specific degree pattern detected in text.")

        st.markdown("---")

        # Skills Categorization
        st.markdown("### 🛠️ Categorized Skills")
        categorized = parsed_data["skills"]["categorized_skills"]
        if categorized:
            for cat_name, skill_list in categorized.items():
                st.markdown(f"**{cat_name}** ({len(skill_list)})")
                badges_html = " ".join([f'<span class="skill-badge">{s}</span>' for s in skill_list])
                st.markdown(badges_html, unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
        else:
            st.warning("No skills matched against the skill taxonomy.")

        st.markdown("---")

        # ATS Matcher Section
        st.markdown("### 🎯 Job Match & ATS Score Calculator")
        default_jd = "We are seeking a Senior Data Scientist / Software Engineer proficient in Python, PyTorch, TensorFlow, SQL, Docker, AWS, NLP, and Git."
        jd_input = st.text_area("Target Job Description / Key Requirements:", value=default_jd, height=100)

        if st.button("Calculate ATS Match Score", type="primary"):
            ats_result = parser.calculate_ats_score(parsed_data, jd_input)
            
            score = ats_result["ats_score"]
            st.subheader(f"ATS Match Score: {score}%")
            st.progress(min(score / 100.0, 1.0))
            
            if score >= 80:
                st.success(ats_result["recommendation"])
            elif score >= 50:
                st.warning(ats_result["recommendation"])
            else:
                st.error(ats_result["recommendation"])

            res_c1, res_c2 = st.columns(2)
            with res_c1:
                st.markdown("**Matched Required Skills:**")
                st.write(", ".join(ats_result["matched_skills"]) if ats_result["matched_skills"] else "None")
            with res_c2:
                st.markdown("**Missing Required Skills:**")
                st.write(", ".join(ats_result["missing_skills"]) if ats_result["missing_skills"] else "None")

        st.markdown("---")
        st.markdown("### 📥 Export Parsing Results")
        exp_col1, exp_col2 = st.columns(2)
        with exp_col1:
            json_str = json.dumps(parsed_data, indent=2)
            st.download_button("Download JSON Output", json_str, file_name=f"{filename}_parsed.json", mime="application/json")
        with exp_col2:
            flat_df = pd.DataFrame([{
                "Filename": parsed_data["filename"],
                "Name": parsed_data["name"],
                "Email": parsed_data["email"],
                "Phone": parsed_data["phone"],
                "Skills": ", ".join(parsed_data["skills"]["all_skills"]),
                "Skill Count": parsed_data["skills"]["total_skills_count"],
                "Experience (Yrs)": parsed_data["experience"]["estimated_years"]
            }])
            csv_data = flat_df.to_csv(index=False).encode('utf-8')
            st.download_button("Download CSV Output", csv_data, file_name=f"{filename}_parsed.csv", mime="text/csv")

    else:
        st.info("👈 Upload a resume or select a test resume from the dropdown above to view results.")

# ---------------------------------------------------------
# TAB 2: BATCH RESUME PARSER & CANDIDATE RANKING
# ---------------------------------------------------------
with tab2:
    st.subheader("👥 Batch Resume Processing & Candidate Comparison")
    
    batch_files = st.file_uploader("Upload Multiple Resumes (PDF / DOCX)", type=["pdf", "docx"], accept_multiple_files=True, key="batch_uploader")
    use_samples = st.checkbox("Include 5 Sample Test Resumes in Batch", value=st.session_state.get("load_samples", False))

    batch_jd = st.text_area("Target Job Description for Candidate Ranking:", 
                            value="Looking for a Python Developer with experience in Django, FastAPI, SQL, Docker, REST API, Git, and Unit Testing.", height=90)

    if st.button("🚀 Process Batch & Rank Candidates", type="primary"):
        resumes_to_process = []

        if use_samples and os.path.exists(SAMPLE_DIR):
            for sname in sample_files:
                spath = os.path.join(SAMPLE_DIR, sname)
                with open(spath, "rb") as f:
                    resumes_to_process.append((io.BytesIO(f.read()), sname))

        if batch_files:
            for bfile in batch_files:
                resumes_to_process.append((bfile, bfile.name))

        if not resumes_to_process:
            st.warning("Please upload files or check 'Include 5 Sample Test Resumes'.")
        else:
            with st.spinner(f"Processing {len(resumes_to_process)} resumes in batch..."):
                batch_results = []
                table_rows = []

                for f_src, f_name in resumes_to_process:
                    p_data = parser.parse(f_src, f_name)
                    ats_info = parser.calculate_ats_score(p_data, batch_jd)
                    p_data["ats_match"] = ats_info
                    batch_results.append(p_data)

                    table_rows.append({
                        "Candidate Name": p_data["name"],
                        "File": p_data["filename"],
                        "ATS Score (%)": ats_info["ats_score"],
                        "Skills Count": p_data["skills"]["total_skills_count"],
                        "Est. Exp (Yrs)": p_data["experience"]["estimated_years"],
                        "Email": p_data["email"],
                        "Phone": p_data["phone"],
                        "Top Skills": ", ".join(p_data["skills"]["all_skills"][:6])
                    })

                df_batch = pd.DataFrame(table_rows).sort_values(by="ATS Score (%)", ascending=False)
                
                st.session_state["df_batch"] = df_batch
                st.session_state["batch_results"] = batch_results

    if "df_batch" in st.session_state:
        df_batch = st.session_state["df_batch"]
        batch_results = st.session_state["batch_results"]

        st.success(f"Batch Processing Complete! Processed {len(df_batch)} candidates.")

        # Summary Metrics
        bm1, bm2, bm3 = st.columns(3)
        with bm1:
            st.metric("Total Candidates", len(df_batch))
        with bm2:
            st.metric("Avg ATS Score", f"{df_batch['ATS Score (%)'].mean():.1f}%")
        with bm3:
            st.metric("Top Candidate", df_batch.iloc[0]["Candidate Name"])

        st.markdown("### 🏆 Candidate Ranking Leaderboard")
        st.dataframe(df_batch, use_container_width=True, height=280)

        # Batch Export
        st.markdown("### 📤 Export Batch Data")
        b_col1, b_col2 = st.columns(2)
        with b_col1:
            csv_batch = df_batch.to_csv(index=False).encode('utf-8')
            st.download_button("Download Candidate Summary CSV", csv_batch, "candidate_ranking_summary.csv", "text/csv")
        with b_col2:
            json_batch = json.dumps(batch_results, indent=2)
            st.download_button("Download Full Batch JSON", json_batch, "candidate_batch_parsed.json", "application/json")

# ---------------------------------------------------------
# TAB 3: SKILL ANALYTICS
# ---------------------------------------------------------
with tab3:
    st.subheader("📊 Skill Distribution & Candidate Insights")

    if "batch_results" in st.session_state and st.session_state["batch_results"]:
        batch_results = st.session_state["batch_results"]
        
        all_skills_list = []
        cat_counts = {}

        for p in batch_results:
            all_skills_list.extend(p["skills"]["all_skills"])
            for cat, sks in p["skills"]["categorized_skills"].items():
                cat_counts[cat] = cat_counts.get(cat, 0) + len(sks)

        # Frequency dataframe
        skill_counts = pd.Series(all_skills_list).value_counts().reset_index()
        skill_counts.columns = ["Skill", "Frequency"]

        col_a1, col_a2 = st.columns(2)

        with col_a1:
            st.markdown("#### 🔝 Top 10 Most Common Skills")
            st.bar_chart(skill_counts.set_index("Skill").head(10))

        with col_a2:
            st.markdown("#### 🏷️ Skill Category Breakdown")
            cat_df = pd.DataFrame(list(cat_counts.items()), columns=["Category", "Total Mentions"])
            st.dataframe(cat_df, use_container_width=True)

    else:
        st.info("💡 Run 'Batch Resume Processing' in Tab 2 to view interactive skill analytics and frequency distributions.")

# ---------------------------------------------------------
# TAB 4: PROJECT REPORT & SPECS
# ---------------------------------------------------------
with tab4:
    st.subheader("📑 Internship Project Report & Documentation")
    st.markdown("*(Elevate Labs Task — Project No. 1: Smart Resume Parser)*")

    report_html = """
    <div class="section-card">
        <h3>1. Abstract</h3>
        <p>The <b>Smart Resume Parser</b> is an automated natural language processing (NLP) system designed to extract, structure, and analyze unstructured information from resumes submitted in PDF and DOCX formats. By combining PyMuPDF, python-docx, spaCy entity recognition, and regex taxonomy matching, the system extracts candidate contact details, skills, education, and experience while offering ATS job match scoring and export capabilities.</p>
        
        <h3>2. Introduction</h3>
        <p>Manual review of hundreds of unstructured resumes is time-consuming and subjective. The Smart Resume Parser converts unstructured PDF/DOCX resumes into structured tabular and JSON data formats, empowering recruiters to rank candidates and visualize skill distributions efficiently.</p>
        
        <h3>3. Tools & Technologies Used</h3>
        <ul>
            <li><b>Python 3.14:</b> Core language logic</li>
            <li><b>PyMuPDF & python-docx:</b> PDF & DOCX text extraction</li>
            <li><b>spaCy & Regex:</b> Named Entity Recognition (PERSON) and skill taxonomy matching</li>
            <li><b>Streamlit:</b> Web application interface</li>
            <li><b>ReportLab:</b> Automated 2-page PDF report generation</li>
        </ul>

        <h3>4. Steps Involved in Building the Project</h3>
        <ol>
            <li>Document Text Extraction for PDF and DOCX</li>
            <li>Text Cleaning & Preprocessing</li>
            <li>Entity & Contact Extraction (Email, Phone, LinkedIn, GitHub)</li>
            <li>Categorized Skill Taxonomy Matching</li>
            <li>Education & Experience Section Parsing</li>
            <li>ATS Compatibility Match Engine</li>
            <li>Streamlit UI & Batch Processing Dashboard</li>
            <li>Automated PDF Report Generation</li>
        </ol>

        <h3>5. Conclusion</h3>
        <p>The project successfully meets all requirements, providing an accurate, scalable, and user-friendly resume parsing system.</p>
    </div>
    """
    st.markdown(report_html, unsafe_allow_html=True)
