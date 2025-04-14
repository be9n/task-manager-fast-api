import sys
import os
import pytest
from fastapi.testclient import TestClient

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app

client = TestClient(app)

@pytest.fixture(scope="module")
def created_task():
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "This is a test task"
    })
    assert response.status_code == 200
    return response.json()

def test_create_task(created_task):
    assert "id" in created_task
    assert created_task["title"] == "Test Task"
    assert created_task["is_done"] is False

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_task_by_id(created_task):
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

def test_update_task(created_task):
    task_id = created_task["id"]
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Updated Task Title",
        "description": "Updated description",
        "is_done": False
    })
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Task Title"
    assert data["description"] == "Updated description"
    assert data["is_done"] is False

def test_mark_task_done(created_task):
    task_id = created_task["id"]
    response = client.patch(f"/tasks/{task_id}/done")
    assert response.status_code == 200
    data = response.json()
    assert data["is_done"] is True

def test_delete_task(created_task):
    task_id = created_task["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id

def test_get_deleted_task(created_task):
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
