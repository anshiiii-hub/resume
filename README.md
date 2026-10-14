# resume

My resume as a small Flask web app: a styled page for people, and a plain-text version for applicant tracking systems (ATS). Both are generated from the same data, so they never drift apart.

## What it serves

- `/` is the styled resume page, with a typewriter-style role animation.
- `/resume.txt` is a clean plain-text resume (summary, skills, experience, projects, education) meant for ATS uploads and easy copy-paste.

## Updating the content

All the content lives in Python dictionaries at the top of `app.py` (`PROFILE`, `SKILLS`, `EXPERIENCE`, `PROJECTS`, `EDUCATION`, `CERT_NOTE`). Edit them once and both versions update. A section with no entries is simply left out of the plain-text version.

## Tech

Python · Flask (3.x) · Jinja templates · HTML and CSS

## Run it locally

```bash
git clone https://github.com/anshiiii-hub/resume.git
cd resume
pip install -r requirements.txt
python app.py
```

Then open http://localhost:5000, or http://localhost:5000/resume.txt for the plain-text version.
