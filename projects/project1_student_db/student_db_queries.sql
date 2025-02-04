-- Insert sample students
INSERT INTO students (name, age, grade) VALUES 
('Alice', 22, 'A'), 
('Bob', 23, 'B'), 
('Charlie', 21, 'A');

-- Insert sample courses
INSERT INTO courses (course_name, instructor) VALUES 
('Mathematics', 'Dr. Smith'),
('Computer Science', 'Prof. Johnson'),
('Physics', 'Dr. Brown');

-- Enroll students in courses
INSERT INTO enrollments (student_id, course_id) VALUES 
(1, 1),  -- Alice in Mathematics
(2, 2),  -- Bob in CS
(3, 1),  -- Charlie in Mathematics
(1, 3);  -- Alice in Physics

-- Retrieve all students and their courses
SELECT students.name, courses.course_name 
FROM students
JOIN enrollments ON students.id = enrollments.student_id
JOIN courses ON enrollments.course_id = courses.course_id;

-- Count students in each grade
SELECT grade, COUNT(*) AS student_count FROM students GROUP BY grade;
