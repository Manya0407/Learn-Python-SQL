import sqlite3

# Connect to the SQLite database (or create if it doesn't exist)
conn = sqlite3.connect("student_db.sqlite")
cursor = conn.cursor()

# Create tables
cursor.executescript("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER CHECK (age > 0),
        grade TEXT CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
    );

    CREATE TABLE IF NOT EXISTS courses (
        course_id INTEGER PRIMARY KEY AUTOINCREMENT,
        course_name TEXT NOT NULL,
        instructor TEXT NOT NULL
    );

    CREATE TABLE IF NOT EXISTS enrollments (
        enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
        FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
    );
""")

# Insert sample data
cursor.executemany("INSERT INTO students (name, age, grade) VALUES (?, ?, ?)", 
                   [("Alice", 22, "A"), ("Bob", 23, "B"), ("Charlie", 21, "A")])

cursor.executemany("INSERT INTO courses (course_name, instructor) VALUES (?, ?)", 
                   [("Mathematics", "Dr. Smith"), ("Computer Science", "Prof. Johnson"), ("Physics", "Dr. Brown")])

cursor.executemany("INSERT INTO enrollments (student_id, course_id) VALUES (?, ?)", 
                   [(1, 1), (2, 2), (3, 1), (1, 3)])

conn.commit()

# Fetch and display students with their enrolled courses
cursor.execute("""
    SELECT students.name, courses.course_name 
    FROM students
    JOIN enrollments ON students.id = enrollments.student_id
    JOIN courses ON enrollments.course_id = courses.course_id
""")
enrollments = cursor.fetchall()

print("Students and their enrolled courses:")
for name, course in enrollments:
    print(f"{name} is enrolled in {course}")

# Close the connection
conn.close()
