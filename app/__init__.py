from flask import Flask
from app.routes import bp as tasks_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(tasks_bp, url_prefix='/api')
    return app