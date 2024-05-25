"""All the resources related to teachers
"""
import os
import json
from flask_restful import Resource
from src.config import ApplicationConfig
from src.utilities.db_utilility import (connect_to_postgres_db1,
                                        get_query_results_as_df
                                        )

app_config = ApplicationConfig(config_path=os.path.join('.', 'config.json'))


class Teacher(Resource):
    """Create Teacher resource
    Args:
        Resource (_type_): Teacher Resource
    """
    def get(self, value=None):
        """Define get method for teachers resource

        Args:
            value (_type_, optional): Teachers id. Defaults to None.

        Returns:
            _type_: _description_
        """
        try:
            con = connect_to_postgres_db1()
            df1 = get_query_results_as_df(con, f"""
                                        SELECT * FROM teacher
                                        where id = {value};"""
                                          ) # noqa
            x = df1.to_json(orient="records") # noqa
            x = json.loads(x)
            con.close()
            # return {
            #     "id": value,
            #     "name": "Just A., Teacher",
            #     "subjects": ["Maths", "Chemistry"],
            #     "schoolName": app_config.get_school_name()
            # }
            return x[0], 200
        except (IndexError, KeyError, ValueError):
            return {'message': 'Teacher not found'}, 404

    def post(self, value=None):
        """Define post method for teachers resource

        Args:
            value (_type_, optional): Teachers id. Defaults to None.
        Returns:
            _type_: Response
        """
        try:
            con = connect_to_postgres_db1()
            _ = get_query_results_as_df(con, f"""
                                        SELECT * FROM teacher
                                        where id = {value};"""
                                        )
            return "Teacher Created", 201

        except (IndexError, KeyError, ValueError):
            return {'message': 'Teacher not created'}, 500
