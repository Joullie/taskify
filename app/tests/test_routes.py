import pytest
from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Limpa a lista de tarefas antes de cada teste
        from app.models import tasks
        tasks.clear()
        yield client

def test_create_task(client):
    response = client.post('/api/tasks', json={"title": "Test Task"})
    assert response.status_code == 201
    assert response.json['title'] == "Test Task"
    assert response.json['completed'] == False

def test_get_tasks(client):
    client.post('/api/tasks', json={"title": "Task 1"})
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert len(response.json) == 1

def test_update_task(client):
    client.post('/api/tasks', json={"title": "Task 1"})
    response = client.put('/api/tasks/1', json={"title": "Updated Task", "completed": True})
    assert response.status_code == 200
    assert response.json['title'] == "Updated Task"
    assert response.json['completed'] == True

def test_complete_task(client):
    client.post('/api/tasks', json={"title": "Task 1"})
    response = client.post('/api/tasks/1/complete')
    assert response.status_code == 200
    assert response.json['completed'] == True

def test_delete_task(client):
    client.post('/api/tasks', json={"title": "Task 1"})
    response = client.delete('/api/tasks/1')
    assert response.status_code == 200
    assert response.json['message'] == "Task deleted"