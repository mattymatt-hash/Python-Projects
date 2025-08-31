import sqlite3
from sqlite3 import Error


def create_connection(db):
    """ Connect to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db)
        print(f"SQLite version: {sqlite3.version}")
        return conn
    except Error as err:
        print(f"Connection error: {err}")
    return None


def create_tables(conn):
    """Create person and student tables if they do not exist"""
    try:
        sql_person = '''
        CREATE TABLE IF NOT EXISTS person (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL
        )'''

        sql_student = '''
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY,
            major TEXT NOT NULL,
            begin_date TEXT
        )'''

        cur = conn.cursor()
        cur.execute(sql_person)
        cur.execute(sql_student)
        conn.commit()
        print("Tables created (if not existed).")
    except Error as e:
        print(f"Error creating tables: {e}")


def create_person(conn, person):
    """Create a new person record"""
    sql = ''' INSERT INTO person(firstname, lastname)
              VALUES(?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, person)
    conn.commit()
    return cur.lastrowid


def create_student(conn, student):
    """Create a new student record"""
    sql = ''' INSERT INTO student(id, major, begin_date)
              VALUES(?, ?, ?) '''
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


if __name__ == '__main__':
    database = "pythonsqlite.db"
    conn = create_connection(database)

    if conn:
        try:
            create_tables(conn)

            person = ('Rob', 'Thomas')
            person_id = create_person(conn, person)

            student = (person_id, 'Songwriting', '2000-01-01')
            student_id = create_student(conn, student)

            print(f"Inserted person ID: {person_id}")
            print(f"Inserted student ID: {student_id}")
        except Error as e:
            print(f"An error occurred during data insertion: {e}")
        finally:
            conn.close()
            print("Connection closed.")
