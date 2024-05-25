from datetime import timedelta, timezone, datetime
from flask import Blueprint
from flask_restful import Api
from .resources.teacher_resources import Teacher

def create_teacher_bp() -> Blueprint:
    teacher_bp= Blueprint('teacher_api', __name__ , url_prefix= '/teacher' )
    api= Api(teacher_bp)
    # Add reasources
    api.add_resource(Teacher, '/', '/<string:value>')
    return teacher_bp