"""_summary_
"""
# from flask_restful import reqparse
from typing import List
from typing_extensions import Annotated

from webargs import fields  # , validate
import marshmallow as ma

# Pydantic implementaion Imports
from pydantic import BaseModel, field_validator
from pydantic.functional_validators import AfterValidator

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


# Pydantic classes
class SubjectQueryModel(BaseModel): # noqa
    sid: int

class Subjects(BaseModel): # noqa
    subject: str
    intructor: str

class SubjectResponseModel(BaseModel): # noqa
    subjects: List[Subjects]
