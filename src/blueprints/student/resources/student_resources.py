"""Creates Resource for Student
"""

import os
import json
from flask_restful import Resource
from flask import request
from webargs.flaskparser import use_kwargs
from marshmallow import ValidationError
from flask_pydantic import validate   # pydantic import
from src.blueprints.student.parsers import student_parsers  # noqa
from src.config import ApplicationConfig
from src.utilities.db_utilility import (connect_to_postgres_db1,
                                        get_query_results_as_df,
                                        insert_dict_to_db
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
            con = connect_to_postgres_db1()
            insert_dict_to_db(students_data, "student", con)
            con.close()
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
            con = connect_to_postgres_db1()
            for student_data in students_data:
                insert_dict_to_db(student_data, "student", con)
            con.close()
            return students_data, 201
        except ValidationError as e:
            return {'message': str(e)}, 400
        except (IndexError, KeyError, ValueError):
            return {'message': 'Could no create students'}, 500


class SubjectsEnrolled(Resource):
    """_summary_

    Args:
        Resource (_type_): _description_
    """
    @validate()
    def get(self, query: student_parsers.SubjectQueryModel):
        """_summary_

        Returns:
            _type_: _description_
        """
        print(query.sid)
        if query.sid == 0:
            return "id cannot be zero", 400
        test_subject = student_parsers.Subjects(
            subject="History",
            intructor="Teacher A"
        )
        list_of_subjects = [test_subject]
        return student_parsers.SubjectResponseModel(
            subjects=list_of_subjects
        ), 200

    @validate()
    def post(self, body: student_parsers.Subjects):
        """_summary_

        Returns:
            _type_: _description_
        """
        print(body.subject)
        return "Enrolled in subject", 201
