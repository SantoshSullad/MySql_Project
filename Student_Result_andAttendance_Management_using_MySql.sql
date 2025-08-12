-- Create Database
CREATE DATABASE IF NOT EXISTS CollegeDB;
USE CollegeDB;

-- Students Table
CREATE TABLE IF NOT EXISTS Students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    dept VARCHAR(50),
    admission_date DATE
);

-- Courses Table
CREATE TABLE IF NOT EXISTS Courses (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_name VARCHAR(100) NOT NULL,
    credits INT CHECK (credits > 0)
);

-- Results Table
CREATE TABLE IF NOT EXISTS Results (
    result_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

-- Attendance Table
CREATE TABLE IF NOT EXISTS Attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT,
    course_id INT,
    attendance_date DATE,
    status ENUM('Present', 'Absent'),
    FOREIGN KEY (student_id) REFERENCES Students(student_id),
    FOREIGN KEY (course_id) REFERENCES Courses(course_id)
);

INSERT INTO Students (name, email, dept, admission_date) VALUES
('John Doe', 'john@example.com', 'CS', '2022-08-10'),
('Alice Smith', 'alice@example.com', 'IT', '2021-09-12'),
('Michael Johnson', 'michaelj@example.com', 'ECE', '2023-01-15'),
('Sophia Brown', 'sophia.brown@example.com', 'CS', '2022-07-18'),
('David Lee', 'david.lee@example.com', 'ME', '2020-06-20'),
('Olivia Miller', 'olivia.miller@example.com', 'IT', '2021-08-05'),
('William Davis', 'william.davis@example.com', 'ECE', '2023-02-25'),
('Emma Wilson', 'emma.wilson@example.com', 'CS', '2022-03-30');

INSERT INTO Courses (course_name, credits) VALUES
('Database Systems', 4),
('Operating Systems', 3),
('Computer Networks', 3),
('Data Structures', 4),
('Software Engineering', 3);

INSERT INTO Results (student_id, course_id, grade) VALUES
(1, 1, 'A'), (1, 2, 'B'), (1, 3, 'A'),
(2, 1, 'B'), (2, 4, 'A'),
(3, 2, 'C'), (3, 5, 'B'),
(4, 1, 'A'), (4, 3, 'B'), (4, 4, 'B'),
(5, 2, 'B'), (5, 3, 'C'),
(6, 1, 'A'), (6, 5, 'A'),
(7, 4, 'B'), (7, 5, 'A'),
(8, 1, 'A'), (8, 2, 'A'), (8, 3, 'B'), (8, 4, 'A');

INSERT INTO Attendance (student_id, course_id, attendance_date, status) VALUES
(1, 1, '2025-08-01', 'Present'),
(1, 1, '2025-08-02', 'Absent'),
(1, 2, '2025-08-01', 'Present'),
(2, 1, '2025-08-01', 'Present'),
(2, 4, '2025-08-02', 'Absent'),
(3, 2, '2025-08-01', 'Present'),
(3, 5, '2025-08-02', 'Present'),
(4, 1, '2025-08-01', 'Present'),
(4, 3, '2025-08-02', 'Absent'),
(5, 2, '2025-08-01', 'Absent'),
(5, 3, '2025-08-02', 'Present'),
(6, 1, '2025-08-01', 'Present'),
(6, 5, '2025-08-02', 'Present'),
(7, 4, '2025-08-01', 'Present'),
(7, 5, '2025-08-02', 'Absent'),
(8, 1, '2025-08-01', 'Present'),
(8, 2, '2025-08-02', 'Present'),
(8, 3, '2025-08-03', 'Absent'),
(8, 4, '2025-08-04', 'Present');

SELECT * FROM Students;
SELECT * FROM Courses;

-- Show Students with Their Grades
SELECT s.name, c.course_name, r.grade
FROM Students as s
JOIN Results as r ON s.student_id = r.student_id
JOIN Courses as c ON r.course_id = c.course_id;

-- Students Who Got Grade 'A'
SELECT s.name, c.course_name
FROM Students s
JOIN Results r ON s.student_id = r.student_id
JOIN Courses c ON r.course_id = c.course_id
WHERE r.grade = 'A';

-- Show Attendance Records
SELECT s.name, c.course_name, a.attendance_date, a.status
FROM Attendance a
JOIN Students s ON a.student_id = s.student_id
JOIN Courses c ON a.course_id = c.course_id;

-- All 'CS' Department Students
SELECT name, dept
FROM Students
WHERE dept = 'CS';

-- Count of Students in Each Department
SELECT dept, COUNT(*) AS total_students
FROM Students
GROUP BY dept;

-- Students With More Than 2 Courses
SELECT student_id, COUNT(course_id) AS course_count
FROM Results
GROUP BY student_id
HAVING course_count > 2;

