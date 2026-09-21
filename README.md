# 🏫 School Management System

A command-line School Management System built with Python using Object-Oriented Programming (OOP).

The system allows users to manage students, teachers, and courses, enroll students in courses, validate user input, and save data permanently using JSON files.

---

## ✨ Features

- Add new students
- Add new teachers
- Add new courses
- Enroll students in courses
- Prevent duplicate student, teacher, and course IDs
- Verify that students and courses exist before enrollment
- Display all registered students
- Display all available courses
- Validate user input
- Handle errors using exceptions
- Save and load data using JSON files

---

## 🧠 Concepts Applied

This project demonstrates the use of:

- Object-Oriented Programming (OOP)
- Classes and objects
- Encapsulation
- Dictionaries and lists
- Functions and methods
- File handling
- JSON data persistence
- Input validation
- Exception handling
- Python modules
- `pathlib` for file paths

---

## 📁 Project Structure

```text
python-school-management-system/
│
├── school_management_system/
│   ├── main.py
│   ├── school.py
│   ├── student.py
│   ├── teacher.py
│   ├── course.py
│   ├── email.py
│   ├── students.json
│   ├── teachers.json
│   └── courses.json
│
└── README.md
```

---

## 🧩 Main Classes

### Student

Stores student information, including:

- Student name
- Age
- Student ID
- Enrolled courses

Main methods:

- `enroll_course()`
- `drop_course()`
- `display_info()`

### Teacher

Stores teacher information, including:

- Teacher ID
- Name
- Subject taught

### Course

Stores course information, including:

- Course code
- Course title
- Assigned teacher
- Enrolled student IDs

Main methods:

- `add_student()`
- `remove_student()`
- `display_course_info()`

### School

Controls the main system operations and manages:

- Students
- Teachers
- Courses
- Student enrollment
- Saving and loading JSON data

---

## 📋 System Menu

When the program starts, the following options are displayed:

```text
1. Add Student
2. Add Course
3. Add Teacher
4. Enroll Student
5. View Students
6. View Courses
7. Exit
```

---

## 💾 Data Storage

The system stores its data in JSON files:

- `students.json`
- `teachers.json`
- `courses.json`

The data is automatically loaded when the program starts and saved after changes are made.

The system also handles missing files and invalid JSON data to prevent unexpected crashes.

---

## ✅ Input Validation

The program validates user input to ensure that:

- Names contain valid characters
- Age is entered as a number
- IDs and course codes are not duplicated
- Students exist before enrollment
- Courses exist before enrollment
- Students are not enrolled in the same course twice

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/itssara1/python-school-management-system.git
```

### 2. Open the project directory

```bash
cd python-school-management-system
```

### 3. Open the application folder

```bash
cd school_management_system
```

### 4. Run the program

```bash
python main.py
```

No external packages are required.

---

## 🛠️ Technologies Used

- Python
- JSON
- Object-Oriented Programming
- Git
- GitHub

---

## 🚀 Future Improvements

Possible future improvements include:

- Adding a graphical user interface
- Adding student grades and attendance
- Creating login accounts for administrators
- Adding search and filtering features
- Connecting the system to a database
- Developing a web version using Django

---

## 👩🏻‍💻 Author

**Sara Alshammari**

Information Technology Graduate  
Python Web Development Trainee at Tuwaiq Academy

---

## 📄 Project Information

This project was developed as part of the Python Web Development Bootcamp at Tuwaiq Academy.
