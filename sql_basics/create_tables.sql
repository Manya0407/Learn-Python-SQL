-- Lesson 2: Creating Tables in SQL

-- Create a "courses" table
CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name VARCHAR(100),
    instructor VARCHAR(50)
);

-- Insert some sample courses
INSERT INTO courses (course_name, instructor) VALUES 
('Mathematics', 'Dr. Smith'),
('Computer Science', 'Prof. Johnson'),
('Physics', 'Dr. Brown');

-- View all courses
SELECT * FROM courses;
