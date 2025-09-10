from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)

def test_visualize_success_td():
    """TD 方向の成功ケース"""
    resp = client.post("/visualization/visualize", json={"content": "A -> B -> C"})
    assert resp.status_code == 200
    assert resp.json()["status"] == "success"

def test_visualize_success_lr():
    """LR 方向の成功ケース"""
    resp = client.post("/visualization/visualize", json={"content": "A -> B", "direction": "LR"})
    assert resp.status_code == 200
    assert "graph LR;" in resp.json()["data"]["mermaid"]

def test_visualize_empty_input():
    """空入力は 400 エラー"""
    resp = client.post("/visualization/visualize", json={"content": "   "})
    assert resp.status_code == 400

def test_visualize_bad_direction():
    """不正な方向は 400 エラー"""
    resp = client.post("/visualization/visualize", json={"content": "A -> B", "direction": "DOWN"})
    assert resp.status_code == 400

