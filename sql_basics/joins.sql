-- Lesson 4: SQL Joins

-- Create an enrollments table
CREATE TABLE enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    student_id INT,
    course_id INT,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

-- Insert sample enrollments
INSERT INTO enrollments (student_id, course_id) VALUES
(1, 1),
(2, 2),
(3, 1);

-- INNER JOIN: Retrieve student names and their courses
SELECT students.name, courses.course_name 
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.course_id;
