🎓 Student Result & Attendance Management System
This project is a desktop application built using Python (Tkinter) and MySQL to manage student details, academic results, and attendance records.
It provides a simple GUI interface for database operations and academic reporting.

🚀 Features
CRUD Operations for Students
Add, Update, Delete, Search, Show All (searchable by ID or Name).

Reports Module:
Show All Students (basic details).
Show All Results (Student + Course + Grade).
Show All Attendance (Student + Course + Date + Status).
Attendance by Student (searchable by ID or Name).
Database Integrity
Primary/Foreign keys and constraints for data consistency.

User-friendly GUI
Built using Tkinter with tabs for Students and Reports.

🛠️ Technologies Used
Python (Tkinter for GUI, mysql-connector for DB connection)

MySQL (Database backend for storing students, courses, results, and attendance)

📂 Project Structure
CollegeDB_FullApp.py → Main Python GUI application.

StudentDB.sql → SQL script to create and initialize the database.

⚡ How to Run
Install requirements:
pip install mysql-connector-python
Create the database in MySQL using the StudentDB.sql file.

Update your MySQL username/password inside CollegeDB_FullApp.py.

Run the app:
python CollegeDB_FullApp.py
