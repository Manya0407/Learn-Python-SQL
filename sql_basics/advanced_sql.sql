-- Lesson 5: Advanced SQL Queries

-- Group students by grade and count them
SELECT grade, COUNT(*) AS student_count
FROM students
GROUP BY grade;

-- Subquery: Find students enrolled in 'Mathematics'
SELECT name FROM students
WHERE id IN (
    SELECT student_id FROM enrollments
    WHERE course_id = (SELECT course_id FROM courses WHERE course_name = 'Mathematics')
);

-- Using CASE for conditional logic
SELECT name, 
    CASE 
        WHEN age < 22 THEN 'Young'
        ELSE 'Older'
    END AS age_group
FROM students;
