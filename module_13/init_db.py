import sqlite3

# Create or connect to the database
conn = sqlite3.connect("pythonsqlite.db")
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS person (
        id INTEGER PRIMARY KEY,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL
    );
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        major TEXT NOT NULL,
        begin_date TEXT NOT NULL,
        end_date TEXT,
        FOREIGN KEY (id) REFERENCES person (id)
    );
""")

# Add a test person and student
cursor.execute("INSERT INTO person (firstname, lastname) VALUES (?, ?)", ('Rob', 'Thomas'))
person_id = cursor.lastrowid

cursor.execute("INSERT INTO student (id, major, begin_date) VALUES (?, ?, ?)",
               (person_id, 'Songwriting', '2000-01-01'))

conn.commit()
conn.close()

print("Tables created and sample data added.")
