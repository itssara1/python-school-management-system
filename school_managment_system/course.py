class Course:
    def __init__(self, course_code, course_title, teacher):
        self.course_code = course_code
        self.course_title = course_title
        self.teacher = teacher
        self.student_ids = []

    def add_student(self, student_id):
        self.student_ids.append(student_id)

    def remove_student(self, student_id):
        self.student_ids.remove(student_id)

    def display_course_info(self):
        return f"""Course information:
Title: {self.course_title}
Code: {self.course_code}
Assigned Teacher: {self.teacher}
Students: {self.student_ids}
"""


# course1 = Course('C001','Python','PY001')
# course1.add_student('S001')
# course1.add_student('S002')
# course1.add_student('S003')
# print(course1.display_course_info())
# course1.remove_student('S003')
# print(course1.display_course_info())
