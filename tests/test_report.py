# tests/test_report.py

"""Report API のテスト"""

from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_generate_report_success():
    """正常入力"""
    response = client.post(
        "/report/generate",
        json={"content": "今日は三つのタスクを完了しました。設計、テスト、バグ修正。"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "markdown" in data["data"]

def test_generate_report_empty_content():
    """空文字入力"""
    response = client.post("/report/generate", json={"content": ""})
    assert response.status_code == 400
    data = response.json()
    assert "detail" in data

def test_generate_report_missing_content():
    """content フィールド欠落"""
    response = client.post("/report/generate", json={})
    assert response.status_code == 422
    data = response.json()
    assert "detail" in data
 

