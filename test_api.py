# test_api.py

from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

@pytest.fixture
def sample_todo():
    return {"title": "Test Todo", "description": "Test Description"}

def test_create_todo(sample_todo):
    response = client.post("/todos/", json=sample_todo)
    assert response.status_code == 200
    assert response.json()["title"] == "Test Todo"

def test_update_todo(sample_todo):
    # Create a todo first
    create_response = client.post("/todos/", json=sample_todo)
    todo_id = create_response.json()["id"]

    # Update the created todo
    updated_todo = {"title": "Updated Todo", "description": "Updated Description"}
    response = client.put(f"/todos/{todo_id}", json=updated_todo)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"

def test_delete_todo(sample_todo):
    # Create a todo first
    create_response = client.post("/todos/", json=sample_todo)
    todo_id = create_response.json()["id"]

    # Delete the created todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted"
