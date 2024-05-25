"""
main module for the flask app
"""
import os

from flask import Flask
from dotenv import load_dotenv

# inporting the blueprintsd
from src.blueprints.student.student import create_student_bp
from src.blueprints.teacher.teacher import create_teacher_bp
from .config import ApplicationConfig

# load env file
load_dotenv(dotenv_path=os.path.join('.', '.env'))

# load config from json
app_config = ApplicationConfig(config_path=os.path.join('.', 'config.json'))


def create_app() -> Flask:
    """
    creates a flask app and registers all the blueprints
    Returns:
        Flask: Flask App
    """
    # Create Falsk app
    app = Flask(__name__)

    # Register all the blueprints
    teacher_bp = create_teacher_bp()
    app.register_blueprint(teacher_bp)

    student_bp = create_student_bp()
    app.register_blueprint(student_bp)

    return app


def main():
    """Creates a Flask app and runs it on the specified port.
    """
    app = create_app()
    app.run(port=int(os.environ.get('PORT', 80)))


if __name__ == "__main__":
    main()
