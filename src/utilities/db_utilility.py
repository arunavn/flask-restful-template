import os
import psycopg2
import pandas as pd

# from dotenv import load_dotenv
# load_dotenv(dotenv_path=os.path.join('.', '.env'))

def connect_to_postgres_db1() -> psycopg2.extensions.connection:
    """Connects to a PostgreSQL database.
    Returns:
        A psycopg2 connection object.
    """
    conn = psycopg2.connect(
        host=os.getenv("DB1_HOST", "localhost"),
        port=os.getenv("DB1_PORT", '5432'),
        dbname=os.getenv("DB1_NAME", "postgres"),
        user=os.getenv("DB1_USERNAME", "postgres"),
        password=os.getenv("DB1_PASSWORD", "")
    )
    return conn

def get_query_results_as_df(con: psycopg2.extensions.connection, query: str) -> pd.DataFrame:
    df = pd.read_sql(query, con)
    return df

# con = connect_to_postgres_db1()
# df1 = get_query_results_as_df(con, "SELECT * FROM student;")
# x = df1.to_json(orient="records")

# import json
# x = json.loads(x)
# print(x)
# con.close()