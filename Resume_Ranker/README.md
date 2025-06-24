# project2
# 🤖 AIviHire – AI-Powered Resume Ranker

AIviHire is an intelligent web-based system that automates resume screening using NLP techniques. Upload multiple resumes, compare them against a job description (e.g., Data Scientist), and get ranked results based on relevance.

---

## 📌 Features

- 📄 Upload multiple resumes in PDF format
- 🔍 NLP-based ranking using TF-IDF + cosine similarity
- 📊 Visual score chart (Chart.js)
- 📥 Download HR report as CSV
- 💬 AIVi Assistant chatbot to answer user queries
- 🌌 Futuristic animated background (particles.js)
- 🌓 Dark/Light theme toggle

---

## 🧰 Tools & Libraries Used

| Tool             | Purpose                                 |
|------------------|------------------------------------------|
| Python           | Core backend logic                       |
| Flask            | Web framework                            |
| SpaCy            | Text preprocessing & NLP                 |
| Scikit-learn     | TF-IDF vectorizer + cosine similarity    |
| PyPDF2           | PDF text extraction                      |
| Chart.js         | Score chart visualization                |
| Particles.js     | Background animation                     |
| HTML/CSS/JS      | UI, chatbot behavior                     |

---

## 🚀 How It Works

1. Upload one or more resumes in PDF format
2. The system extracts and cleans the text using SpaCy
3. Uses TF-IDF to convert resumes and job description into vectors
4. Cosine similarity is used to score each resume
5. Displays results in a table and a bar chart
6. Download CSV report with scores
7. Chatbot provides real-time help

---

## 📁 Project Structure
```
AIviHire/
├── resume.py # Flask backend
├── job_description.txt # Predefined JD used for comparison
├── resumes/ # Folder to upload resumes
├── output/ # Generated CSV report
├── static/
│ ├── style.css
│ ├── script.js
│ ├── chatbot.js
│ ├── particles.min.js
│ └── particles-config.js
├── templates/
│ ├── start.html
│ └── index.html
| ├── home.html
| ├── chatbot.html
├── require.txt
└── README.md

```
---
## 📸 Sample Outputs

### 🏠 Dashboard Interface
![Home page](https://github.com/Patel-Riya-D/Projects/blob/main/Resume_Ranker/home_page.png)

### 🌌 User Interface
![UI](https://github.com/Patel-Riya-D/Projects/blob/main/Resume_Ranker/UI.png)

### 📊 Ranking Table
![Ranking Table](https://github.com/Patel-Riya-D/Projects/blob/main/Resume_Ranker/ranking_result.png)

### 📈 Score Chart
![Score Chart](https://github.com/Patel-Riya-D/Projects/blob/main/Resume_Ranker/score_chart.png)


### 💬 AIVi Assistant in Action
![Chatbot](https://github.com/Patel-Riya-D/Projects/blob/main/Resume_Ranker/chatbot.png)

---

## 🌐 Deployment (Localhost)
http://127.0.0.1:5000

### ▶️ Run locally:
```bash
pip install -r require.txt
python app.py

