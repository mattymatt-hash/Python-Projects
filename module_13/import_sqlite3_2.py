import sqlite3
from sqlite3 import Error
import tkinter as tk
from tkinter import ttk, messagebox, font


# Database functions (reuse your existing code here)
def create_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except Error as err:
        print(err)
    return None


def create_tables(conn):
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
        begin_date TEXT,
        FOREIGN KEY(id) REFERENCES person(id)
    )'''
    cur = conn.cursor()
    cur.execute(sql_person)
    cur.execute(sql_student)
    conn.commit()


def create_person(conn, person):
    sql = 'INSERT INTO person(firstname, lastname) VALUES (?, ?)'
    cur = conn.cursor()
    cur.execute(sql, person)
    conn.commit()
    return cur.lastrowid


def create_student(conn, student):
    sql = 'INSERT INTO student(id, major, begin_date) VALUES (?, ?, ?)'
    cur = conn.cursor()
    cur.execute(sql, student)
    conn.commit()
    return cur.lastrowid


def select_all_persons(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM person")
    return cur.fetchall()


def select_all_students(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM student")
    return cur.fetchall()


def find_person_id(conn, firstname, lastname):
    cur = conn.cursor()
    cur.execute("SELECT id FROM person WHERE firstname=? AND lastname=?", (firstname, lastname))
    result = cur.fetchone()
    return result[0] if result else None


# GUI Application
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Person & Student Manager")
        self.geometry("700x600")
        self.configure(bg="#f0f4f8")

        # Set a nice font
        self.default_font = font.nametofont("TkDefaultFont")
        self.default_font.configure(size=10)

        self.conn = create_connection("pythonsqlite.db")

        # Widgets
        self.create_widgets()

    def create_widgets(self):
        # Frame for DB controls
        db_frame = tk.Frame(self, bg="#d9e6f2", pady=10, padx=10)
        db_frame.pack(fill=tk.X, padx=10, pady=5)
        tk.Button(db_frame, text="Create Database & Tables", command=self.create_db, bg="#4a90e2", fg="white", relief="raised", font=('Helvetica', 11, 'bold')).pack()

        # Frame for Add Person
        person_frame = tk.LabelFrame(self, text="Add Person", bg="#ffffff", fg="#333333", font=('Helvetica', 12, 'bold'), padx=10, pady=10)
        person_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(person_frame, text="First Name:", bg="#ffffff").grid(row=0, column=0, sticky='w', pady=2)
        self.person_fname = tk.Entry(person_frame, width=30)
        self.person_fname.grid(row=0, column=1, pady=2, padx=5)

        tk.Label(person_frame, text="Last Name:", bg="#ffffff").grid(row=1, column=0, sticky='w', pady=2)
        self.person_lname = tk.Entry(person_frame, width=30)
        self.person_lname.grid(row=1, column=1, pady=2, padx=5)

        tk.Button(person_frame, text="Add Person", command=self.add_person, bg="#4a90e2", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

        # Frame for Add Student
        student_frame = tk.LabelFrame(self, text="Add Student", bg="#ffffff", fg="#333333", font=('Helvetica', 12, 'bold'), padx=10, pady=10)
        student_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(student_frame, text="First Name:", bg="#ffffff").grid(row=0, column=0, sticky='w', pady=2)
        self.student_fname = tk.Entry(student_frame, width=30)
        self.student_fname.grid(row=0, column=1, pady=2, padx=5)

        tk.Label(student_frame, text="Last Name:", bg="#ffffff").grid(row=1, column=0, sticky='w', pady=2)
        self.student_lname = tk.Entry(student_frame, width=30)
        self.student_lname.grid(row=1, column=1, pady=2, padx=5)

        tk.Label(student_frame, text="Major:", bg="#ffffff").grid(row=2, column=0, sticky='w', pady=2)
        self.student_major = tk.Entry(student_frame, width=30)
        self.student_major.grid(row=2, column=1, pady=2, padx=5)

        tk.Label(student_frame, text="Start Date (YYYY-MM-DD):", bg="#ffffff").grid(row=3, column=0, sticky='w', pady=2)
        self.student_startdate = tk.Entry(student_frame, width=30)
        self.student_startdate.grid(row=3, column=1, pady=2, padx=5)

        tk.Button(student_frame, text="Add Student", command=self.add_student, bg="#4a90e2", fg="white").grid(row=4, column=0, columnspan=2, pady=10)

        # Frame for View Buttons and output
        view_frame = tk.Frame(self, bg="#d9e6f2", pady=10, padx=10)
        view_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        btn_frame = tk.Frame(view_frame, bg="#d9e6f2")
        btn_frame.pack(fill=tk.X)

        tk.Button(btn_frame, text="View Person Table", command=self.view_persons, bg="#50b948", fg="white", font=('Helvetica', 10, 'bold')).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="View Student Table", command=self.view_students, bg="#f39c12", fg="white", font=('Helvetica', 10, 'bold')).pack(side=tk.LEFT, padx=5)
        tk.Button(btn_frame, text="Exit", command=self.destroy, bg="#e74c3c", fg="white", font=('Helvetica', 10, 'bold')).pack(side=tk.RIGHT, padx=5)

        # Text box for output with scrollbar
        self.output = tk.Text(view_frame, height=15, font=('Consolas', 11))
        self.output.pack(fill=tk.BOTH, expand=True, pady=10, side=tk.LEFT)

        scrollbar = ttk.Scrollbar(view_frame, command=self.output.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.output.config(yscrollcommand=scrollbar.set)

    def create_db(self):
        if self.conn:
            create_tables(self.conn)
            messagebox.showinfo("Success", "Database and tables created (if not existed).")

    def add_person(self):
        fname = self.person_fname.get().strip()
        lname = self.person_lname.get().strip()
        if not fname or not lname:
            messagebox.showwarning("Input error", "Please enter first and last name for the person.")
            return
        person = (fname, lname)
        person_id = create_person(self.conn, person)
        messagebox.showinfo("Success", f"Person added with ID: {person_id}")

    def add_student(self):
        fname = self.student_fname.get().strip()
        lname = self.student_lname.get().strip()
        major = self.student_major.get().strip()
        startdate = self.student_startdate.get().strip()
        if not (fname and lname and major and startdate):
            messagebox.showwarning("Input error", "Please fill all student fields.")
            return
        person_id = find_person_id(self.conn, fname, lname)
        if not person_id:
            messagebox.showerror("Error", "Person not found! Add the person first.")
            return
        student = (person_id, major, startdate)
        create_student(self.conn, student)
        messagebox.showinfo("Success", f"Student added for Person ID: {person_id}")

    def view_persons(self):
        self.output.delete('1.0', tk.END)
        persons = select_all_persons(self.conn)
        self.output.insert(tk.END, "ID | First Name | Last Name\n")
        self.output.insert(tk.END, "-" * 30 + "\n")
        for p in persons:
            self.output.insert(tk.END, f"{p[0]:<3}| {p[1]:<12}| {p[2]}\n")

    def view_students(self):
        self.output.delete('1.0', tk.END)
        students = select_all_students(self.conn)
        self.output.insert(tk.END, "Person ID | Major         | Start Date\n")
        self.output.insert(tk.END, "-" * 40 + "\n")
        for s in students:
            self.output.insert(tk.END, f"{s[0]:<9}| {s[1]:<13}| {s[2]}\n")


if __name__ == "__main__":
    app = App()
    app.mainloop()
