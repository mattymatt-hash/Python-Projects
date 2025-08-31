"""
* Name         : program name  atabase gui assignment
* Author       : Matthew Stevens
* Created      : Creation Date 7-15-2025
* Course       : CIS189
* IDE          : Visual Studio Code
* Description  : The purpose of this program is basically crud. "    create read update delete"     input is name first and last major and dates and the output is when theyu are viewed.
*
* Academic Honesty: I attest that this is my original work.
* I have not used unauthorized source code, either modified or
* unmodified.
"""
import sqlite3
import tkinter as tk
from tkinter import messagebox

#  DATABASE FUNCTIONS 

def create_db_and_tables():
    conn = sqlite3.connect("school.db")
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS person (
                    person_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    firstname TEXT NOT NULL,
                    lastname TEXT NOT NULL
                )''')

    c.execute('''CREATE TABLE IF NOT EXISTS student (
                    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    person_id INTEGER,
                    major TEXT,
                    startdate TEXT,
                    FOREIGN KEY (person_id) REFERENCES person(person_id)
                )''')

    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Database and tables created.")

def create_person(firstname, lastname):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    c.execute("INSERT INTO person (firstname, lastname) VALUES (?, ?)", (firstname, lastname))
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", f"Person '{firstname} {lastname}' added.")

def create_student(firstname, lastname, major, startdate):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()

    c.execute("SELECT person_id FROM person WHERE firstname = ? AND lastname = ?", (firstname, lastname))
    result = c.fetchone()
    if result:
        person_id = result[0]
        c.execute("INSERT INTO student (person_id, major, startdate) VALUES (?, ?, ?)",
                  (person_id, major, startdate))
        conn.commit()
        messagebox.showinfo("Success", f"Student '{firstname} {lastname}' added.")
    else:
        messagebox.showerror("Error", "Person not found. Add them first.")

    conn.close()

def view_table(table_name):
    conn = sqlite3.connect("school.db")
    c = conn.cursor()
    if table_name == "person":
        c.execute("SELECT * FROM person")
    elif table_name == "student":
        c.execute('''SELECT student.student_id, person.firstname, person.lastname, student.major, student.startdate
                     FROM student JOIN person ON student.person_id = person.person_id''')
    else:
        conn.close()
        return []

    rows = c.fetchall()
    conn.close()
    return rows

#  GUI SETUP 

root = tk.Tk()
root.title("Database and GUI Assignment")

#  INPUT FIELDS 
tk.Label(root, text="First Name").grid(row=0, column=0)
entry_first = tk.Entry(root)
entry_first.grid(row=0, column=1)

tk.Label(root, text="Last Name").grid(row=1, column=0)
entry_last = tk.Entry(root)
entry_last.grid(row=1, column=1)

tk.Label(root, text="Major").grid(row=2, column=0)
entry_major = tk.Entry(root)
entry_major.grid(row=2, column=1)

tk.Label(root, text="Start Date").grid(row=3, column=0)
entry_start = tk.Entry(root)
entry_start.grid(row=3, column=1)

# DISPLAY AREA  
output = tk.Text(root, height=10, width=60)
output.grid(row=6, column=0, columnspan=3, pady=10)

# BUTTON FUNCTIONS 

def add_person_gui():
    firstname = entry_first.get().strip()
    lastname = entry_last.get().strip()
    if firstname and lastname:
        create_person(firstname, lastname)
    else:
        messagebox.showerror("Input Error", "First and Last name required.")

def add_student_gui():
    firstname = entry_first.get().strip()
    lastname = entry_last.get().strip()
    major = entry_major.get().strip()
    startdate = entry_start.get().strip()
    if firstname and lastname and major and startdate:
        create_student(firstname, lastname, major, startdate)
    else:
        messagebox.showerror("Input Error", "All fields  required for student.")

def view_persons():
    output.delete(1.0, tk.END)
    rows = view_table("person")
    for row in rows:
        output.insert(tk.END, f"{row}\n")

def view_students():
    output.delete(1.0, tk.END)
    rows = view_table("student")
    for row in rows:
        output.insert(tk.END, f"{row}\n")

# --- BUTTONS ---
tk.Button(root, text="Create Database & Table", command=create_db_and_tables).grid(row=4, column=0, pady=5)
tk.Button(root, text="Add Person", command=add_person_gui).grid(row=4, column=1, pady=5)
tk.Button(root, text="Add Student", command=add_student_gui).grid(row=4, column=2, pady=5)
tk.Button(root, text="View Person Table", command=view_persons).grid(row=5, column=0, pady=5)
tk.Button(root, text="View Student Table", command=view_students).grid(row=5, column=1, pady=5)
tk.Button(root, text="Exit", command=root.destroy).grid(row=5, column=2, pady=5)

root.mainloop()
