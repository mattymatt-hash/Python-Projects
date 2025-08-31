import sqlite3
from sqlite3 import Error

def create_connection(db):
    """ Connect to a SQLite database
    :param db: filename of database
    :return connection if no error, otherwise None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def create_table(conn, sql_create_table):
    """ Creates table with given SQL statement
    :param conn: Connection object
    :param sql_create_table: a SQL CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_create_table)
    except Error as e:
        print(e)

def create_tables(database):
    sql_create_person_table = """ CREATE TABLE IF NOT EXISTS person (
                                        id integer PRIMARY KEY,
                                        firstname text NOT NULL,
                                        lastname text NOT NULL
                                    ); """

    sql_create_student_table = """CREATE TABLE IF NOT EXISTS student (
                                    id integer PRIMARY KEY,
                                    major text NOT NULL,
                                    begin_date text NOT NULL,
                                    end_date text,
                                    FOREIGN KEY (id) REFERENCES person (id)
                                );"""

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_person_table)
        create_table(conn, sql_create_student_table)
    else:
        print("Unable to connect to " + str(database))

def create_person(conn, person):
    """Create a new person for table
    :param conn:
    :param person:
    :return: person id
    """
    sql = ''' INSERT INTO person(firstname,lastname)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, person)
    return cur.lastrowid

def create_student(conn, student):
    """Create a new student for table
    :param conn:
    :param student:
    :return: student id
    """
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    return cur.lastrowid

def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return: list of rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    return rows

def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return: list of rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    db_file = "pythonsqlite.db"
    create_tables(db_file)

    conn = create_connection(db_file)
    with conn:
        # Insert sample data if tables are empty
        if not select_all_persons(conn):
            person = ('Rob', 'Thomas')
            person_id = create_person(conn, person)

            student = (person_id, 'Songwriting', '2000-01-01')
            create_student(conn, student)

        print("Persons:")
        for row in select_all_persons(conn):
            print(row)

        print("\nStudents:")
        for row in select_all_students(conn):
            print(row)
