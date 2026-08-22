class Student:
    def __init__(self, name, age, student_id):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        elif not name.isalpha():
            raise ValueError("Name Must contain leeters only")

        self.name = name

        if not 0 < age:
            raise ValueError("Age must be greater than 0")

        self.age = age

        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)

    def drop_course(self, course):
        self.courses.remove(course)

    def display_info(self):
        return f"""Student Name: {self.name}
Student Age: {self.age}
Student ID: {self.student_id}
Enrolled Courses: {self.courses}
"""


# student1 = Student('Sara', 21, 'S001')
# student1.enroll_course('Python')
# student1.enroll_course('JS')
# student1.enroll_course('CSS')
# # print(student1.courses)
# student1.drop_course('JS')
# # print(student1.courses)
# print(student1.display_info())
