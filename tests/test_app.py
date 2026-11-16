import os
import sys

# Ensure repository root is on sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Ensure a mock key exists for testing so Groq client initializes
if not os.environ.get("GROQ_API_KEY"):
    os.environ["GROQ_API_KEY"] = "mock_test_key_for_ci_pipeline"

import pytest
from app import app, load_questions

def test_questions_dataset_structure():
    assert os.path.exists("AI_interview_questions.csv")
    df = load_questions()
    assert len(df) > 0
    assert "question" in df.columns
    assert "answer" in df.columns

def test_homepage_route():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200

def test_api_stats():
    client = app.test_client()
    res = client.get("/api/stats")
    assert res.status_code == 200
    data = res.get_json()
    assert "total" in data
    assert data["total"] > 0
