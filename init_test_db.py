"""## to setup local postgress follow: https://medium.com/@nathaliafriederichs/setting-up-a-postgresql-environment-in-docker-a-step-by-step-guide-55cbcb1061ba
"""
import psycopg2


def connect_to_postgres(host, database, user, password):
    """Connects to a PostgreSQL database.

    Args:
        host: The host name or IP address of the database server.
        database: The name of the database to connect to.
        user: The username to use for the connection.
        password: The password to use for the connection.

    Returns:
        A psycopg2 connection object.
    """

    conn = psycopg2.connect(
        host=host,
        dbname=database,
        user=user,
        password=password
    )

    return conn

con = connect_to_postgres("localhost", 'postgres', 'postgres', 'my_password' )
print(type(con))
# Execute a command: this creates a teacher
cur = con.cursor()
cur.execute('DROP TABLE IF EXISTS teacher;')
cur.execute('CREATE TABLE teacher (id serial PRIMARY KEY,'
                                 'name varchar (50) NOT NULL,'
                                 'subjects varchar (300) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )

# Insert data into the teacher table
cur.execute('INSERT INTO teacher (name, subjects)'
            'VALUES (%s, %s)',
            ('Just A., Teacher',
             'Maths, Chemistry')
            )

cur.execute('INSERT INTO teacher (name, subjects)'
            'VALUES (%s, %s)',
            ('Just B., Teacher',
             'Maths, History')
            )

# Add Student

# Create student table
cur.execute('DROP TABLE IF EXISTS student;')
cur.execute('CREATE TABLE student (id serial PRIMARY KEY,'
                                 'name varchar (50) NOT NULL,'
                                 'father_name varchar (300) NOT NULL,'
                                 'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                 )


# Insert data into the student table
cur.execute('INSERT INTO student (name, father_name)'
            'VALUES (%s, %s)',
            ('Just A., Student',
             'Just A., Father')
            )

cur.execute('INSERT INTO student (name, father_name)'
            'VALUES (%s, %s)',
            ('Just B., Student',
             'Just B., Father')
            )



con.commit()    
cur.close()
con.close()


## Validate
con = connect_to_postgres("localhost", 'postgres', 'postgres', 'my_password' )
cursor = con.cursor()
cursor.execute("CREATE TABLE new_table (id INT PRIMARY KEY, name VARCHAR(50));")

cursor = con.cursor()
cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema='public';")

for table in cursor.fetchall():
    print(table[0])

cursor = con.cursor()
cursor.execute("SELECT * FROM student;")

for table in cursor.fetchall():
    print(table)
cursor.close()
con.close()


