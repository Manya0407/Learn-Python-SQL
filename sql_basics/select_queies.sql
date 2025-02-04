-- Lesson 3: Basic SQL Queries

-- Select all students
SELECT * FROM students;

-- Select specific columns
SELECT name, grade FROM students;

-- Filter results
SELECT * FROM students WHERE grade = 'A';

-- Count the number of students
SELECT COUNT(*) FROM students;
