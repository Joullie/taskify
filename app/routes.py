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