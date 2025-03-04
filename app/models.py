import json
import os

class Task:
    def __init__(self, id, title, completed=False):
        self.id = id
        self.title = title
        self.completed = completed

    def to_dict(self):
        return {"id": self.id, "title": self.title, "completed": self.completed}

TASKS_FILE = os.path.join(os.path.dirname(__file__), '..', 'tasks.json')

def load_tasks():
    if not os.path.exists(TASKS_FILE) or os.path.getsize(TASKS_FILE) == 0:
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"Conteúdo lido: {content}")  # Adiciona log para depurar
            tasks_data = json.loads(content)
            return [Task(t['id'], t['title'], t['completed']) for t in tasks_data]
    except (json.JSONDecodeError, UnicodeDecodeError) as e:
        print(f"Erro ao carregar tasks.json: {e}")
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1