"""Creates Resource for Student
"""

import os
import json
from flask_restful import Resource
from src.config import ApplicationConfig
from src.utilities.db_utilility import (connect_to_postgres_db1,
                                        get_query_results_as_df
                                        )

app_config = ApplicationConfig(config_path=os.path.join('.', 'config.json'))


class Student(Resource):
    """Creates Student Resource

    Args:
        Resource (_type_): Student resource
    """
    def get(self, value=None):
        """Define get method for student resource

        Args:
            value (_type_, optional): Teachers id. Defaults to None.

        Returns:
            _type_: response
        """
        try:
            con = connect_to_postgres_db1()
            df1 = get_query_results_as_df(con, f"""
                                        SELECT * FROM student
                                        where id = {value};"""
                                          ) # noqa
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

    def post(self, value=None):
        """Define post method for student resource

        Args:
            value (_type_, optional): Teachers id. Defaults to None.

        Returns:
            _type_: rsponse
        """
        try:
            con = connect_to_postgres_db1()
            _ = get_query_results_as_df(con, f"""
                                        SELECT * FROM student
                                        where id = {value};"""
                                        )
            return "Student Created", 201
        except (IndexError, KeyError, ValueError):
            return {'message': 'student not created'}, 500
