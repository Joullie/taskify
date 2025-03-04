from flask import Blueprint, request, jsonify
from app.models import Task, load_tasks, save_tasks, get_next_id

bp = Blueprint('tasks', __name__)

@bp.route('/tasks', methods=['POST'])
def create_task():
    tasks = load_tasks()
    data = request.get_json()
    if not data or 'title' not in data or not isinstance(data['title'], str):
        return jsonify({"error": "Valid title is required"}), 400
    task = Task(get_next_id(tasks), data['title'])
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task.to_dict()), 201

@bp.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = load_tasks()
    return jsonify([task.to_dict() for task in tasks]), 200

@bp.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    tasks = load_tasks()
    data = request.get_json()
    for task in tasks:
        if task.id == task_id:
            if 'title' in data and isinstance(data['title'], str):
                task.title = data['title']
            if 'completed' in data and isinstance(data['completed'], bool):
                task.completed = data['completed']
            save_tasks(tasks)
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

@bp.route('/tasks/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task.id == task_id:
            task.completed = True
            save_tasks(tasks)
            return jsonify(task.to_dict()), 200
    return jsonify({"error": "Task not found"}), 404

@bp.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            save_tasks(tasks)
            return jsonify({"message": "Task deleted"}), 200
    return jsonify({"error": "Task not found"}), 404