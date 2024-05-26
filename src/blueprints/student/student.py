"""Creates studdent blueprint and adds resources
"""
from flask import Blueprint
from flask_restful import Api
from src.blueprints.student.resources import student_resources


def create_student_bp() -> Blueprint:
    """Creates student blueprint and adds resources

    Returns:
        Blueprint: _description_
    """
    student_bp = Blueprint('student_api', __name__, url_prefix='/student')
    api = Api(student_bp)

    # Add resources
    api.add_resource(student_resources.Student, '/')
    api.add_resource(student_resources.Students, '/students')
    return student_bp
