import pytest
import os
import pandas as pd
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
