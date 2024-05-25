import os 
from flask_restful import Resource
from flask import jsonify, request
import json
from src.config import ApplicationConfig
from src.utilities.db_utilility import connect_to_postgres_db1, get_query_results_as_df


app_config = ApplicationConfig(config_path=os.path.join('.', 'config.json'))

class Student(Resource):
    def get(self, value=None):
        try:
            con = connect_to_postgres_db1()
            df1 = get_query_results_as_df(con, f"SELECT * FROM student where id = {value};")
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
        except:
            return {'message': 'student not found' }, 404 

    def post(self, value=None):
        try:
            return "Student Created", 201
        except:
            return {'message': 'student not created' }, 500