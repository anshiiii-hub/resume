from flask import Flask, render_template, Response, send_file
from datetime import datetime
import json

app = Flask(__name__)

# ---------------------------------------------------------------------------
# All resume content lives in ONE place. This does two jobs:
#   1. Feeds the HTML site (templates/index.html)
#   2. Feeds the plain-text ATS resume export (/resume.txt route)
# Keeping a single source of truth means the site and the ATS export can
# never drift out of sync with each other.
# ---------------------------------------------------------------------------

PROFILE = {
    "name": "Anshita Dawar",
    "title": "Data Science Intern",
    "subtitle": "AI Engineer Bootcamp co-instructor — Open to Data Science Internships",
    "location": "Haryana, India",
    "email": "anshitadawar90@gmail.com",  # NOTE: fixed apparent typo (gmai.com -> gmail.com) — please confirm
    "phone": "+91-9588596043",
    "linkedin": "linkedin.com/in/anshita-dawar",
    "linkedin_url": "https://www.linkedin.com/in/anshita-dawar",
    "summary": (
        "I'm a student working my way into data science, currently deep in an AI Engineer "
        "Bootcamp and interning at CodroidHub Pvt. Ltd., where I build real, working "
        "projects rather than just following along. That's meant shipping seven AI-powered "
        "Flask web apps and getting hands-on with Python, SQL, Power BI and Tableau on real "
        "problem statements. I'm not pretending to have it all figured out — I'm looking for "
        "a Data Science internship where I can keep learning by doing."
    ),
    "now_badge": "Right now: AI Engineer Bootcamp \u00b7 Interning at CodroidHub Pvt. Ltd. \u00b7 Open to internships",
    "sticky_note": "still figuring it out, one dataset at a time",
    "typewriter_roles": ["Data Science Student.", "Aspiring Data Analyst.", "Eager Intern.", "Lifelong Learner."],
}

SKILLS = [
    {"category": "Programming & Analysis", "items": ["Python", "Pandas", "NumPy", "SQL"]},
    {"category": "Machine Learning & NLP", "items": ["Scikit-learn", "NLP", "Sentiment Analysis", "Model Evaluation"]},
    {"category": "BI & Visualization", "items": ["Power BI", "Tableau", "Data Storytelling"]},
    {"category": "Web & Tooling", "items": ["Flask", "Jupyter / nbformat", "BeautifulSoup", "Git"]},
    {"category": "Instructional Design", "items": ["Curriculum Design", "Technical Documentation", "Notebook Authoring"]},
    {"category": "Communication", "items": ["Stakeholder Presentations", "Canva", "Figma"]},
]

EXPERIENCE = [
    {
        "date": "Current",
        "title": "Data Science Intern",
        "org": "CodroidHub Pvt. Ltd.",
        "bullets": [
            "Building real, production-style projects as part of the AI Engineer Bootcamp rather than following tutorials — including 7 AI-powered Flask web apps: meeting minutes generation, document comparison, Gantt chart planning, sentiment analysis, inventory tracking, invoice/marksheet generation, and policy compliance checking.",
            "Practicing end-to-end delivery: idea, data, code, and a working app a reviewer can actually click through.",
            "Picking up applied AI/ML and data analytics skills directly from bootcamp coursework and mentorship.",
        ],
    },
    {
        "date": "Prior",
        "title": "Data Analytics Intern",
        "org": "CodroidHub Pvt. Ltd.",
        "bullets": [
            "Completed six applied problem statements using web scraping, SQL, Python and Power BI.",
            "Built an end-to-end Netflix subscriber data analysis project, turning raw data into a clear visual narrative.",
        ],
    },
    {
        "date": "Prior",
        "title": "Teaching Assistant — Mathematics",
        "org": "",
        "bullets": [
            "Planned and delivered lessons to help students grasp concepts clearly, simplifying complex ideas for individual needs.",
            "Sharpened the same skill I now apply to explaining data insights simply.",
        ],
    },
]

PROJECTS = [
    {
        "name": "AI Meeting Minutes Generator",
        "desc": "Flask app that converts raw meeting transcripts into structured, actionable meeting minutes using an LLM pipeline.",
        "tags": ["Flask", "NLP", "LLM"],
    },
    {
        "name": "Document Comparison Tool",
        "desc": "Compares two documents section by section and surfaces material differences for fast review.",
        "tags": ["Python", "NLP", "Flask"],
    },
    {
        "name": "AI Gantt Chart Planner",
        "desc": "Turns a plain-language project description into a structured Gantt chart with tasks, durations and dependencies.",
        "tags": ["Python", "Project Planning"],
    },
    {
        "name": "Sentiment Analysis Dashboard",
        "desc": "Analyzes text at scale and visualizes sentiment trends for review or feedback data.",
        "tags": ["NLP", "Sentiment Analysis", "Flask"],
    },
    {
        "name": "Inventory Tracking System",
        "desc": "Flask-based inventory tracker with stock-level alerts and simple reporting views.",
        "tags": ["Flask", "SQL"],
    },
    {
        "name": "Invoice / Marksheet Generator",
        "desc": "Generates formatted invoices and marksheets from structured input data.",
        "tags": ["Python", "PDF Generation"],
    },
    {
        "name": "Policy Compliance Checker",
        "desc": "Checks a document against a defined policy set and flags non-compliant clauses.",
        "tags": ["NLP", "Rules Engine"],
    },
    {
        "name": "Netflix Data Analysis",
        "desc": "Exploratory analysis of Netflix subscriber and content data, visualized for a non-technical audience.",
        "tags": ["Pandas", "Power BI"],
    },
]

EDUCATION = [
    # Fill in your actual degree details here, e.g.:
    # {"degree": "B.Tech, Computer Science", "org": "Your University", "date": "2022 - 2026"},
]

CERT_NOTE = "AI Engineer Bootcamp — currently interning at CodroidHub Pvt. Ltd."


@app.route("/")
def index():
    return render_template(
        "index.html",
        profile=PROFILE,
        skills=SKILLS,
        experience=EXPERIENCE,
        projects=PROJECTS,
        education=EDUCATION,
        cert_note=CERT_NOTE,
        year=datetime.now().year,
        typewriter_roles_json=json.dumps(PROFILE["typewriter_roles"]),
    )


@app.route("/resume.txt")
def resume_txt():
    """Plain-text, ATS-parseable resume generated from the same data as the site."""
    lines = []
    lines.append(PROFILE["name"].upper())
    lines.append(PROFILE["title"])
    lines.append(f"{PROFILE['location']} | {PROFILE['email']} | {PROFILE['phone']} | {PROFILE['linkedin']}")
    lines.append("")
    lines.append("SUMMARY")
    lines.append(PROFILE["summary"])
    lines.append("")
    lines.append("SKILLS")
    for group in SKILLS:
        lines.append(f"{group['category']}: {', '.join(group['items'])}")
    lines.append("")
    lines.append("EXPERIENCE")
    for job in EXPERIENCE:
        org_part = f" — {job['org']}" if job.get("org") else ""
        lines.append(f"{job['title']}{org_part} ({job['date']})")
        for b in job["bullets"]:
            lines.append(f"  - {b}")
        lines.append("")
    lines.append("PROJECTS")
    for p in PROJECTS:
        lines.append(f"{p['name']}: {p['desc']} [{', '.join(p['tags'])}]")
    if EDUCATION:
        lines.append("")
        lines.append("EDUCATION")
        for e in EDUCATION:
            lines.append(f"{e['degree']} — {e['org']} ({e['date']})")
    body = "\n".join(lines)
    return Response(body, mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=False)
