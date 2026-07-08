# 🤖 Agentic AI Naukri Profile Updater

An AI-powered automation framework built with **Python**, **Playwright**, and **Agentic AI** to automate Naukri profile updates using a Planner-Agent-Orchestrator architecture.

The project combines traditional UI automation with AI agents to intelligently plan, execute, and validate profile update tasks.

---

## 🚀 Features

- Playwright automation using Python
- Page Object Model (POM) design pattern
- Planner-driven task execution
- Agent-based automation architecture
- Orchestration layer for workflow management
- Logging support
- Environment variable configuration
- Modular and scalable project structure

---

## 📂 Project Structure

```
AgenticAI_NaukriUpdate/
│
├── pom/
│   ├── base_page.py
│   ├── login_page.py
│   ├── profile_page.py
│   └── __init__.py
│
├── scripts/
│   └── profile_automation.py
│
├── planner.py
├── agent.py
├── orchestration.py
├── logger.py
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

- Python
- Playwright
- Page Object Model (POM)
- OpenAI API
- Git
- GitHub

---

## ⚙️ Setup

### Clone Repository

```bash
git clone https://github.com/Dev-anshu1804/AgenticAI_NaukriUpdate.git
```

### Navigate to Project

```bash
cd AgenticAI_NaukriUpdate
```

### Create Virtual Environment

```bash
python -m venv .venv
```

### Activate Virtual Environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Install Playwright Browsers

```bash
playwright install
```

---

## 🔐 Environment Variables

Create a `.env` file using the `.env.example` template.

Example:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Run Automation

```bash
python scripts/profile_automation.py
```

---

## 📌 Current Progress

- ✅ Playwright Automation Framework
- ✅ Page Object Model
- ✅ Planner Module
- ✅ Agent Module
- ✅ Orchestration Module
- ✅ Logging Support

### Upcoming

- AI Validation Agent
- Multi-Agent Collaboration
- Round Robin Group Chat
- Retry & Recovery Mechanism
- Docker Support
- CI/CD Integration

---

## 📈 Future Enhancements

- Resume Analyzer
- AI-based Profile Optimization
- Job Recommendation Agent
- ATS Score Improvement Suggestions
- Multi-job Portal Support

---

## 👩‍💻 Author

**Anshu Singh**

Senior QA Engineer | Python | Playwright | Manual Testing | Agentic AI

GitHub:
https://github.com/Dev-anshu1804