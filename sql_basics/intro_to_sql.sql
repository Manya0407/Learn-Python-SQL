-- Lesson 1: Introduction to SQL
-- Creating a simple database

CREATE DATABASE school;

-- Use the database
USE school;

-- Create a table
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(5)
);

-- Insert sample data
INSERT INTO students (name, age, grade) VALUES 
('Alice', 22, 'A'), 
('Bob', 23, 'B'), 
('Charlie', 21, 'A');

-- Retrieve all students
SELECT * FROM students;
