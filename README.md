# AI Interview Preparation System

An interactive web application for practicing Machine Learning and Data Science interview questions, featuring real-time AI evaluation powered by LLaMA 3.1 via the Groq API.

## Core Features
- **Curated Question Bank**: Search, browse, and filter ML questions across topics and difficulty tiers.
- **Interactive Quiz Drills**: Practice random questions and test recall under interview conditions.
- **AI Feedback**: Automated answer evaluation grading response quality, identifying strengths, and offering tactical tips.
- **Contextual Hints**: Request subtle prompts to assist recall without giving away full solutions.
- **Dataset Extensibility**: Upload new question collections via CSV with automated validation.

## Technical Stack
- **Backend**: Python 3, Flask
- **Data Engine**: Pandas
- **AI Inference**: Groq Cloud SDK (`llama-3.1-8b-instant`)
- **Frontend**: HTML5, Vanilla JavaScript, CSS3
- **Testing**: Pytest

## Quickstart

### 1. Setup Environment
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configure Credentials
Copy `.env.example` to `.env` and set your API key:
```bash
GROQ_API_KEY=your_actual_key_here
```

### 3. Run Application
```bash
python app.py
```
Visit `http://127.0.0.1:5000` in your web browser.

## Testing
```bash
pytest tests/
```
