from student import Student
from course import Course
from teacher import Teacher
import json
from pathlib import Path


class School:
    def __init__(self):
        self.students = {}
        self.courses = {}
        self.teachers = {}

    def add_student(self, student):
        if student.student_id in self.students:
            raise ValueError("Duplicate student ID")

        self.students[student.student_id] = student

    def add_course(self, course):
        if course.course_code in self.courses:
            raise ValueError("Duplicate course code")

        self.courses[course.course_code] = course

    def add_teacher(self, teacher):
        if teacher.teacher_id in self.teachers:
            raise ValueError("Duplicate teacher ID")

        self.teachers[teacher.teacher_id] = teacher

    def enroll_student(self, student_id, course_code):
        if student_id not in self.students:
            raise ValueError("Student not found")
        elif course_code not in self.courses:
            raise ValueError("Course not found")

        student = self.students[student_id]
        course = self.courses[course_code]

        if course_code in student.courses:
            raise ValueError("Student already enrolled in this course")

        student.enroll_course(course_code)
        course.add_student(student_id)

    def display_students(self):
        for student in self.students.values():
            print(student.display_info())

    def display_courses_info(self):
        for course in self.courses.values():
            print(course.display_course_info())

    def drop_student(self, student_id, course_code):
        if student_id not in self.students:
            raise ValueError("Student not found")
        elif course_code not in self.courses:
            raise ValueError("Course not found")

        student = self.students[student_id]
        course = self.courses[course_code]

        if course_code not in student.courses:
            raise ValueError("Student is not enrolled in this course")

        student.drop_course(course_code)
        course.remove_student(student_id)

    def display_teachers(self):
        for teacher in self.teachers.values():
            print(
                f"Teacher ID: {teacher.teacher_id}\n"
                f"Teacher Name: {teacher.name}\n"
                f"Subject taught: {teacher.subject_taught}"
            )

    def save_students(self):
        students_data = []
        for student in self.students.values():
            students_data.append(
                {
                    "student_id": student.student_id,
                    "name": student.name,
                    "age": student.age,
                    "courses": student.courses,
                }
            )
        file_path = Path(__file__).parent / "students.json"

        with open(file_path, "w") as file:
            json.dump(students_data, file, indent=4)

    def save_courses(self):
        courses_data = []

        for course in self.courses.values():
            courses_data.append(
                {
                    "course_code": course.course_code,
                    "course_title": course.course_title,
                    "teacher": course.teacher,
                    "student_ids": course.student_ids,
                }
            )
        file_path = Path(__file__).parent / "courses.json"
        with open(file_path, "w") as file:
            json.dump(courses_data, file, indent=4)

    def save_teachers(self):
        teachers_data = []

        for teacher in self.teachers.values():
            teachers_data.append(
                {
                    "teacher_id": teacher.teacher_id,
                    "name": teacher.name,
                    "subject_taught": teacher.subject_taught,
                }
            )
        file_path = Path(__file__).parent / "teachers.json"

        with open(file_path, "w") as file:
            json.dump(teachers_data, file, indent=4)

    def load_students(self):
        file_path = Path(__file__).parent / "students.json"

        try:
            with open(file_path, "r") as file:
                students_data = json.load(file)

            for data in students_data:
                student = Student(
                    data["name"],
                    data["age"],
                    data["student_id"],
                )

                student.courses = data["courses"]
                self.students[student.student_id] = student
        except FileNotFoundError:
            message = "students.json not found"
            print(message)
            self.log_error(message)

        except json.JSONDecodeError:
            message = "students.json is corrupted"
            print(message)
            self.log_error(message)

        except KeyError:
            message = "students.json has missing fields"
            print(message)
            self.log_error(message)

    def load_courses(self):
        file_path = Path(__file__).parent / "courses.json"
        try:
            with open(file_path, "r") as file:
                courses_data = json.load(file)

            for data in courses_data:
                course = Course(
                    data["course_code"], data["course_title"], data["teacher"]
                )

                course.student_ids = data["student_ids"]
                self.courses[course.course_code] = course

        except FileNotFoundError:
            message = "courses.json not found"
            print(message)
            self.log_error(message)

        except json.JSONDecodeError:
            message = "courses.json is corrupted"
            print(message)
            self.log_error(message)

        except KeyError:
            message = "courses.json has missing fields"
            print(message)
            self.log_error(message)

    def load_teachers(self):
        file_path = Path(__file__).parent / "teachers.json"
        try:
            with open(file_path, "r") as file:
                teachers_data = json.load(file)

            for data in teachers_data:
                teacher = Teacher(
                    data["teacher_id"], data["name"], data["subject_taught"]
                )

            self.teachers[teacher.teacher_id] = teacher

        except FileNotFoundError:
            message = "teachers.json not found"
            print(message)
            self.log_error(message)

        except json.JSONDecodeError:
            message = "teachers.json is corrupted"
            print(message)
            self.log_error(message)

        except KeyError:
            message = "teachers.json has missing fields"
            print(message)
            self.log_error(message)

    def log_error(self, message):
        with open(Path(__file__).parent / "logs.txt", "a") as file:
            file.write(message + "\n")
