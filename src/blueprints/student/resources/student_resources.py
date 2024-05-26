"""Creates Resource for Student
"""

import os
import json
from flask_restful import Resource
from flask import request
from webargs.flaskparser import use_kwargs
from marshmallow import ValidationError
from src.config import ApplicationConfig
from src.blueprints.student.parsers import student_parsers
from src.utilities.db_utilility import (connect_to_postgres_db1,
                                        get_query_results_as_df
                                        )

app_config = ApplicationConfig(config_path=os.path.join('.', 'config.json'))


class Student(Resource):
    """Creates Student Resource

    Args:
        Resource (_type_): Student resource
    """
    @use_kwargs(student_parsers.student_get_parser(), location='query')
    def get(self, **kwargs):
        """Define get method for student resource

        Args:
            value (_type_, optional): Teachers id. Defaults to None.

        Returns:
            _type_: response
        """
        try:
            where_stmt = f"name = '{kwargs.get('name', None)}'"
            sid = kwargs.get('id', None)
            if sid:
                where_stmt = f"id = {sid}"
            con = connect_to_postgres_db1()
            df1 = get_query_results_as_df(con, f"""
                                        SELECT * FROM student
                                        where {where_stmt};"""
                                          )
            x = df1.to_json(orient="records")
            x = json.loads(x)
            con.close()
            # return {
            #     "id": value,
            #     "name": "Just A., Student",
            #     "fatherName": "Just A., Father",
            #     "schoolName": app_config.get_school_name()
            # }
            return x[0], 200
        except (IndexError, KeyError, ValueError):
            return {'message': 'student not found'}, 404

    def post(self):
        """Define post method for student resource

        Args:
            value (_type_, optional): Teachers id. Defaults to None.

        Returns:
            _type_: rsponse
        """
        try:
            students_data = student_parsers.StudentPost(many=False)\
                .load(request.get_json())
            return students_data, 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except (IndexError, KeyError, ValueError):
            return {'message': 'Could no create students'}, 500


class Students(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """

    def get(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            con = connect_to_postgres_db1()
            df1 = get_query_results_as_df(con, "SELECT * FROM student;")
            x = df1.to_json(orient="records")
            x = json.loads(x)
            con.close()
            return x, 200
        except (IndexError, KeyError, ValueError):
            return {'message': 'Could no get students'}, 500

    def post(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        try:
            students_data = student_parsers.StudentPost(many=True)\
                .load(request.get_json())
            return students_data, 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except (IndexError, KeyError, ValueError):
            return {'message': 'Could no create students'}, 500
