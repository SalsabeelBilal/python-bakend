import sqlite3

def init_db():
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        grade REAL
    )
    """)
    conn.commit()
    return conn

def add_student(conn, name, grade):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (name, grade) VALUES (?, ?)", (name, grade))
    conn.commit()

def view_students(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def update_grade(conn, name, new_grade):
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET grade = ? WHERE name = ?", (new_grade, name))
    conn.commit()

def delete_student(conn, name):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name = ?", (name,))
    conn.commit()

if __name__ == "__main__":
    conn = init_db()
    
    add_student(conn, "Ali", 90)
    add_student(conn, "Sara", 85)
    
    print("All students:", view_students(conn))
    
    update_grade(conn, "Ali", 95)
    print("After update:", view_students(conn))
    
    delete_student(conn, "Sara")
    print("After deletion:", view_students(conn))
    
    conn.close()
