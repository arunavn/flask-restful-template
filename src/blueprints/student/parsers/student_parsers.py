# from flask_restful import reqparse
from webargs import fields  # , validate
import marshmallow as ma


def student_get_parser() -> dict:
    """parser for get student
    Returns:
        dict: parser
    """
    user_args = {
        'id': fields.Str(),
        'name': fields.Str()
    }
    return user_args


class StudentPost(ma.Schema):
    """_summary_
    """
    name = ma.fields.String(required=True)
    father_name = ma.fields.String(required=True)
