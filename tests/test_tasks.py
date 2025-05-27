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
    response_json = response.json()
    assert response_json["status_code"] == 201
    assert response_json["success"] is True
    return response_json["data"]

def test_create_task(created_task):
    assert "id" in created_task
    assert created_task["title"] == "Test Task"
    assert created_task["is_done"] is False

def test_get_tasks():
    response = client.get("/tasks/")
    response_json = response.json()
    assert response_json["status_code"] == 200
    assert response_json["success"] is True
    assert isinstance(response_json["data"], list)

def test_get_task_by_id(created_task):
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    response_json = response.json()
    assert response_json["status_code"] == 200
    assert response_json["success"] is True
    data = response_json["data"]
    assert data["id"] == task_id

def test_update_task(created_task):
    task_id = created_task["id"]
    response = client.put(f"/tasks/{task_id}", json={
        "title": "Updated Task Title",
        "description": "Updated description",
        "is_done": False
    })
    response_json = response.json() 
    assert response_json["status_code"] == 200
    assert response_json["success"] is True
    data = response_json["data"]
    assert data["title"] == "Updated Task Title"
    assert data["description"] == "Updated description"
    assert data["is_done"] is False

def test_mark_task_done(created_task):
    task_id = created_task["id"]
    response = client.patch(f"/tasks/{task_id}/done")
    response_json = response.json()
    assert response_json["status_code"] == 200
    assert response_json["success"] is True
    data = response_json["data"]
    assert data["is_done"] is True

def test_delete_task(created_task):
    task_id = created_task["id"]
    response = client.delete(f"/tasks/{task_id}")
    response_json = response.json()
    assert response_json["status_code"] == 200
    assert response_json["success"] is True
    data = response_json["data"]
    assert data["id"] == task_id

def test_get_deleted_task(created_task):
    task_id = created_task["id"]
    response = client.get(f"/tasks/{task_id}")
    response_json = response.json()
    assert response_json["status_code"] == 404
    assert response_json["success"] is False
    assert response_json["data"] is None
    assert len(response_json["errors"]) > 0
