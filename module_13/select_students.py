"""
* Name         : program name select_students.py
* Author       : Matthew Stevens
* Created      : Creation Date 7-10
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is to connect to a sqlite database to get the rows of data. The input is the database The output is the printed database records.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""


import sqlite3
from sqlite3 import Error

def create_connection(db):
    """ Connect to SQLite database
    param  filename of database
    return without error, or None"""
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None

def select_all_persons(conn):
    """select all rows in table
    param the connection 
    return tupleslist
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")
    rows = cur.fetchall()
    return rows

def select_all_students(conn):
    """select all rows in table
    param the connection
    return tuples list
    """
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    return rows

if __name__ == '__main__':
    conn = create_connection("pythonsqlite.db")
    with conn:
        print("=== Person Table ===")
        persons = select_all_persons(conn)
        for row in persons:
            print(row)

        print("\n=== Student Table ===")
        students = select_all_students(conn)
        for row in students:
            print(row)
