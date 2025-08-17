import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------------- MySQL Connection ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",              # your MySQL username
    password="Santosh@1490",  # your MySQL password
    database="CollegeDB"
)
cursor = conn.cursor()

# ---------------- Utility Function ----------------
def refresh_tree(tree, query, headers):
    cursor.execute(query)
    rows = cursor.fetchall()
    tree.delete(*tree.get_children())  # Clear old data
    tree["columns"] = headers
    tree["show"] = "headings"
    for col in headers:
        tree.heading(col, text=col)
        tree.column(col, width=150, anchor="center")
    for row in rows:
        tree.insert("", "end", values=row)

# ---------------- Students CRUD ----------------
def add_student():
    name, email, dept = entry_name.get(), entry_email.get(), entry_dept.get()
    if name and email and dept:
        cursor.execute("INSERT INTO Students (name, email, dept, admission_date) VALUES (%s, %s, %s, CURDATE())",
                       (name, email, dept))
        conn.commit()
        messagebox.showinfo("Success", "Student added!")
        show_students()
    else:
        messagebox.showwarning("Input Error", "Fill all fields!")

def update_student():
    try:
        selected = tree_students.selection()[0]
        sid = tree_students.item(selected)["values"][0]
        name, email, dept = entry_name.get(), entry_email.get(), entry_dept.get()
        cursor.execute("UPDATE Students SET name=%s, email=%s, dept=%s WHERE student_id=%s",
                       (name, email, dept, sid))
        conn.commit()
        messagebox.showinfo("Updated", "Student updated!")
        show_students()
    except:
        messagebox.showwarning("Select Row", "Select a student to update!")

def delete_student():
    try:
        selected = tree_students.selection()[0]
        sid = tree_students.item(selected)["values"][0]
        cursor.execute("DELETE FROM Students WHERE student_id=%s", (sid,))
        conn.commit()
        messagebox.showinfo("Deleted", "Student deleted!")
        show_students()
    except:
        messagebox.showwarning("Select Row", "Select a student to delete!")

def search_student():
    keyword = entry_search.get()
    query = f"SELECT student_id, name, email, dept, admission_date FROM Students WHERE name LIKE '%{keyword}%' OR student_id LIKE '%{keyword}%'"
    refresh_tree(tree_students, query, ("ID","Name","Email","Dept","Admission Date"))

def show_students():
    refresh_tree(tree_students,
        "SELECT student_id, name, email, dept, admission_date FROM Students",
        ("ID","Name","Email","Dept","Admission Date")
    )

# ---------------- Reports ----------------
def show_all_students():
    refresh_tree(tree_report,
        "SELECT name, email, dept, admission_date FROM Students",
        ("Name","Email","Dept","Admission Date")
    )

def show_all_results():
    refresh_tree(tree_report,
        """SELECT s.name, c.course_name, r.grade
           FROM Results r
           JOIN Students s ON r.student_id = s.student_id
           JOIN Courses c ON r.course_id = c.course_id""",
        ("Student Name","Course","Grade")
    )

def show_all_attendance():
    refresh_tree(tree_report,
        """SELECT s.name, c.course_name, a.attendance_date, a.status
           FROM Attendance a
           JOIN Students s ON a.student_id = s.student_id
           JOIN Courses c ON a.course_id = c.course_id""",
        ("Student Name","Course","Date","Status")
    )

def show_attendance_by_student():
    keyword = entry_att_report.get()
    query = f"""SELECT s.name, c.course_name, a.attendance_date, a.status
                FROM Attendance a
                JOIN Students s ON a.student_id = s.student_id
                JOIN Courses c ON a.course_id = c.course_id
                WHERE s.name LIKE '%{keyword}%' OR s.student_id LIKE '%{keyword}%'"""
    refresh_tree(tree_report, query, ("Student Name","Course","Date","Status"))

# ---------------- Main GUI ----------------
root = tk.Tk()
root.title("CollegeDB - Management System")
root.geometry("1000x700")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# ---------- Students Tab ----------
tab_students = ttk.Frame(notebook)
notebook.add(tab_students, text="Students")

frame_s = tk.Frame(tab_students); frame_s.pack(pady=10)

tk.Label(frame_s, text="Name").grid(row=0, column=0); entry_name = tk.Entry(frame_s); entry_name.grid(row=0, column=1)
tk.Label(frame_s, text="Email").grid(row=1, column=0); entry_email = tk.Entry(frame_s); entry_email.grid(row=1, column=1)
tk.Label(frame_s, text="Dept").grid(row=2, column=0); entry_dept = tk.Entry(frame_s); entry_dept.grid(row=2, column=1)

btn_frame = tk.Frame(frame_s); btn_frame.grid(row=3, columnspan=2, pady=5)
tk.Button(btn_frame, text="Add", command=add_student).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Update", command=update_student).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", command=delete_student).grid(row=0, column=2, padx=5)
tk.Button(btn_frame, text="Show All", command=show_students).grid(row=0, column=3, padx=5)

# Search Box
tk.Label(frame_s, text="Search by Name/ID").grid(row=4, column=0)
entry_search = tk.Entry(frame_s); entry_search.grid(row=4, column=1)
tk.Button(frame_s, text="Search", command=search_student).grid(row=4, column=2, padx=5)

# Treeview
tree_students = ttk.Treeview(tab_students)
tree_students.pack(expand=True, fill="both")
show_students()

# ---------- Reports Tab ----------
tab_reports = ttk.Frame(notebook)
notebook.add(tab_reports, text="Reports")

frame_r = tk.Frame(tab_reports); frame_r.pack(pady=10)

tk.Button(frame_r, text="Show All Students", command=show_all_students).grid(row=0, column=0, padx=5)
tk.Button(frame_r, text="Show All Results", command=show_all_results).grid(row=0, column=1, padx=5)
tk.Button(frame_r, text="Show All Attendance", command=show_all_attendance).grid(row=0, column=2, padx=5)

# Attendance by Student
tk.Label(frame_r, text="Enter Student ID or Name:").grid(row=1, column=0, pady=10)
entry_att_report = tk.Entry(frame_r)
entry_att_report.grid(row=1, column=1)
tk.Button(frame_r, text="Show Attendance by Student", command=show_attendance_by_student).grid(row=1, column=2, padx=5)

# Treeview for displaying reports
tree_report = ttk.Treeview(tab_reports)
tree_report.pack(expand=True, fill="both")

root.mainloop()
