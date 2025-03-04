import json
import os

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

# Caminho do arquivo JSON
TASKS_FILE = os.path.join(os.path.dirname(__file__), '..', 'tasks.json')

def load_tasks():
    """Carrega as tarefas do arquivo JSON ou retorna uma lista vazia se não existir."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            tasks_data = json.load(f)
            return [Task(t['id'], t['title'], t['completed']) for t in tasks_data]
    return []

def save_tasks(tasks):
    """Salva as tarefas no arquivo JSON."""
    with open(TASKS_FILE, 'w') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)

def get_next_id(tasks):
    """Retorna o próximo ID disponível."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1