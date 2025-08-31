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


def select_all_persons(conn):
    """Query all rows of person table
    :param conn: the connection object
    :return: list of person rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    return rows


def select_all_students(conn):
    """Query all rows of student table
    :param conn: the connection object
    :return: list of student rows
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    return rows


if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    with conn:
        print("Persons:")
        persons = select_all_persons(conn)
        for person in persons:
            print(person)

        print("\nStudents:")
        students = select_all_students(conn)
        for student in students:
            print(student)
