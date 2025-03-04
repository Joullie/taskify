import json
import os
from datetime import datetime

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = datetime.now().isoformat()  # Timestamp no formato ISO 8601

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at
        }

# Caminho do arquivo JSON
TASKS_FILE = os.path.join(os.path.dirname(__file__), '..', 'tasks.json')

def load_tasks():
    """Carrega as tarefas do arquivo JSON ou retorna uma lista vazia se não existir ou estiver vazio."""
    if not os.path.exists(TASKS_FILE) or os.path.getsize(TASKS_FILE) == 0:
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks_data = json.load(f)
            return [Task(t['id'], t['title'], t.get('completed', False)) for t in tasks_data]
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []

def save_tasks(tasks):
    """Salva as tarefas no arquivo JSON."""
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)

def get_next_id(tasks):
    """Retorna o próximo ID disponível."""
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1