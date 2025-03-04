import json
import os
from datetime import datetime

class Task:
    def __init__(self, id, title, completed=False, created_at=None):
        self.id = id
        self.title = title
        self.completed = completed
        self.created_at = created_at if created_at else datetime.now().isoformat()

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "completed": self.completed,
            "created_at": self.created_at
        }

TASKS_FILE = os.path.join(os.path.dirname(__file__), '..', 'tasks.json')

def load_tasks():
    if not os.path.exists(TASKS_FILE) or os.path.getsize(TASKS_FILE) == 0:
        return []
    try:
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            tasks_data = json.load(f)
            return [Task(t['id'], t['title'], t.get('completed', False), t.get('created_at')) for t in tasks_data]
    except (json.JSONDecodeError, UnicodeDecodeError):
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump([task.to_dict() for task in tasks], f, indent=2)

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task.id for task in tasks) + 1