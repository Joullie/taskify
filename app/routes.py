from flask import Blueprint, request, jsonify
from app.models import Task, tasks, next_id

bp = Blueprint('tasks', __name__)

@bp.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    data = request.get_json()
    if not data or 'title' not in data or not isinstance(data['title'], str):
        return jsonify({"error": "Valid title is required"}), 400
    task = Task(next_id, data['title'])
    tasks.append(task)
    next_id += 1
    return jsonify(task.to_dict()), 201

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify([task.to_dict() for task in tasks]), 200

# ... (código anterior mantido)

@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    for task in tasks:
        if task.id == task_id:
            if 'title' in data and isinstance(data['title'], str):
                task.title = data['title']
            if 'completed' in data and isinstance(data['completed'], bool):
                task.completed = data['completed']
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

@bp.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

# ... (código anterior mantido)

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404

