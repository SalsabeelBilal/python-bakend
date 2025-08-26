import sqlite3

# Connect to database
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    grade REAL
)
""")

# Create
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Ali", 90))
cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", ("Sara", 85))
conn.commit()

# Read
cursor.execute("SELECT * FROM students")
print("Students:", cursor.fetchall())

# Update
cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (95, "Ali"))
conn.commit()

# Delete
cursor.execute("DELETE FROM students WHERE name = ?", ("Sara",))
conn.commit()

# Final check
cursor.execute("SELECT * FROM students")
print("After update & delete:", cursor.fetchall())

conn.close()
