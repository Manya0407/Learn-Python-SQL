-- Create the database (if not using SQLite)
CREATE DATABASE student_db;
USE student_db;

-- Create Students table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT CHECK (age > 0),
    grade VARCHAR(5) CHECK (grade IN ('A', 'B', 'C', 'D', 'F'))
);

-- Create Courses table
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    instructor VARCHAR(50) NOT NULL
);

-- Create Enrollments table (Many-to-Many relationship)
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);
