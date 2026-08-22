from student import Student
from course import Course
from teacher import Teacher

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

    def drop_student(self,  student_id, course_code):
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
        for teacher in  self.teachers.values():
            print(f"Teacher ID: {teacher.teacher_id}\nTeacher Name: {teacher.name}\nSubject taught: {teacher.subject_taught}")


student1 = Student('Sara',21,'S001')
student2 = Student('Areej',23,'S002')
student3 = Student('Lina',23,'S003')


course1 = Course('PY01','Python','C01')
course2 = Course('J101','JS','C02')


teacher1 = Teacher('T01','Faisal','Python')

Tauiq = School()
Tauiq.add_student(student1)
Tauiq.add_student(student2)
Tauiq.add_student(student3)

Tauiq.add_course(course1)
Tauiq.add_course(course2)


Tauiq.add_teacher(teacher1)
# Tauiq.display_students()
# Tauiq.display_courses_info()
# Tauiq.display_teachers()
try:
    Tauiq.enroll_student("S999", "PY01")
except ValueError as error:
    print(error)

Tauiq.enroll_student("S002", "J101")
Tauiq.enroll_student("S003", "PY01")


Tauiq.display_students()
Tauiq.display_courses_info()

#Tauiq.drop_student('S001', 'PY01')
# Tauiq.display_courses_info()
# Tauiq.display_students()

