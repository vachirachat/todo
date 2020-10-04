# tests/test_simple.py

from fastapi.testclient import TestClient
from todo.main import app

client = TestClient(app)


def test_service_info():
    response = client.get("/service_info")
    assert response.status_code == 200
