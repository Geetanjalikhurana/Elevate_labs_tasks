"""
skills_db.py
Taxonomy of technical skills, frameworks, tools, and domain keywords for Smart Resume Parser.
"""

SKILL_TAXONOMY = {
    "Programming Languages": [
        "python", "java", "c++", "c#", "c", "javascript", "typescript", "ruby",
        "php", "swift", "kotlin", "go", "golang", "rust", "r", "scala", "dart",
        "perl", "haskell", "matlab", "bash", "shell", "powershell", "html", "html5",
        "css", "css3", "sql", "pl/sql", "t-sql", "solidity"
    ],
    "Web & Frontend Development": [
        "react", "react.js", "reactjs", "angular", "angularjs", "vue", "vue.js",
        "next.js", "nextjs", "nuxt.js", "svelte", "ember.js", "jquery", "bootstrap",
        "tailwind", "tailwindcss", "sass", "less", "webpack", "vite", "babel",
        "redux", "zustand", "graphql", "rest api", "restful api", "json", "xml"
    ],
    "Backend & Frameworks": [
        "django", "flask", "fastapi", "node.js", "nodejs", "express", "express.js",
        "spring", "spring boot", "asp.net", ".net core", "laravel", "symfony",
        "rails", "ruby on rails", "nest.js", "nestjs", "grpc", "microservices"
    ],
    "Data Science & AI / ML": [
        "machine learning", "deep learning", "artificial intelligence", "nlp",
        "natural language processing", "computer vision", "spacy", "nltk", "transformers",
        "huggingface", "scikit-learn", "sklearn", "tensorflow", "pytorch", "keras",
        "pandas", "numpy", "scipy", "matplotlib", "seaborn", "plotly", "opencv",
        "xgboost", "lightgbm", "catboost", "statsmodels", "data analysis",
        "data visualization", "predictive modeling", "feature engineering",
        "langchain", "llm", "rag", "genai", "prompt engineering"
    ],
    "Databases & Storage": [
        "postgresql", "postgres", "mysql", "sqlite", "mongodb", "redis", "oracle",
        "microsoft sql server", "cassandra", "dynamodb", "neo4j", "elasticsearch",
        "opensearch", "mariadb", "firebase", "supabase", "snowflake", "bigquery"
    ],
    "Cloud & DevOps": [
        "aws", "amazon web services", "azure", "microsoft azure", "gcp",
        "google cloud platform", "docker", "kubernetes", "k8s", "terraform",
        "ansible", "jenkins", "github actions", "gitlab ci", "ci/cd", "helm",
        "prometheus", "grafana", "nginx", "apache", "linux", "ubuntu", "centos"
    ],
    "Tools & Platforms": [
        "git", "github", "gitlab", "bitbucket", "jira", "confluence", "postman",
        "swagger", "figma", "vs code", "pycharm", "jupyter", "jupyter notebook",
        "excel", "power bi", "tableau", "streamlit", "gradio"
    ],
    "Software Engineering & Concepts": [
        "object-oriented programming", "oop", "functional programming", "data structures",
        "algorithms", "system design", "agile", "scrum", "kanban", "unit testing",
        "pytest", "unittest", "integration testing", "test driven development", "tdd",
        "design patterns", "clean code", "code review"
    ],
    "Soft Skills & Management": [
        "communication", "leadership", "teamwork", "problem solving",
        "critical thinking", "project management", "time management",
        "analytical skills", "collaboration", "adaptability", "mentorship"
    ]
}

# Normalize and flat mapping for quick extraction
def get_flat_skill_map():
    """
    Returns a dictionary mapping lowercase skill names to (canonical_name, category)
    """
    flat_map = {}
    for category, skills in SKILL_TAXONOMY.items():
        for skill in skills:
            # Map canonical name (capitalized nicely)
            canonical = skill.strip()
            # Beautify formatting for display
            if canonical in ["c++", "c#", "html", "css", "sql", "aws", "gcp", "nlp", "ai", "ml", "llm", "rag", "api", "json", "xml", "ci/cd", "oop", "tdd"]:
                display_name = canonical.upper()
            elif canonical in ["javascript", "typescript"]:
                display_name = canonical.capitalize()
            elif canonical in ["react.js", "reactjs"]:
                display_name = "React.js"
            elif canonical in ["node.js", "nodejs"]:
                display_name = "Node.js"
            elif canonical in ["next.js", "nextjs"]:
                display_name = "Next.js"
            elif canonical in ["vue.js", "vuejs"]:
                display_name = "Vue.js"
            elif canonical in ["scikit-learn", "sklearn"]:
                display_name = "scikit-learn"
            elif canonical in ["tensorflow"]:
                display_name = "TensorFlow"
            elif canonical in ["pytorch"]:
                display_name = "PyTorch"
            elif canonical in ["postgresql", "postgres"]:
                display_name = "PostgreSQL"
            elif canonical in ["mongodb"]:
                display_name = "MongoDB"
            else:
                display_name = canonical.title()

            flat_map[canonical.lower()] = {
                "display_name": display_name,
                "category": category
            }
    return flat_map
