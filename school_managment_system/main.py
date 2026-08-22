from school import School
from student import Student
from course import Course
from teacher import Teacher

school = School()
school.load_students()
school.load_courses()
school.load_teachers()

while True:
    print("\nSCHOOL MANAGEMENT SYSTEM")
    print("1. Add student")
    print("2. Add course")
    print("3. Add teacher")
    print("4. Enroll student")
    print("5. View students")
    print("6. View courses")
    print("7. Drop course")
    print("8. Exit")

    choice = input("Choose an option: ")

    try:

        if choice == "1":
            name = input("Enter your name: ")
            age = input("Enter your age: ")
            age = int(age)
            student_id = input("Enter your ID: ")
            student = Student(name, age, student_id)
            school.add_student(student)

            print(f"Student {name} added successfully")

        elif choice == "2":
            course_code = input("Enter course code: ")
            course_title = input("Enter course title: ")
            teacher = input("Enter teacher ID: ")
            if teacher not in school.teachers:
                raise ValueError("Teacher not found")
            course = Course(course_code, course_title, teacher)
            school.add_course(course)

            print(f"Course {course_title} added successfully")

        elif choice == "3":
            teacher_id = input("Enter your ID: ")
            name = input("Enter your name: ")
            subject_taught = input("Enter subject taught: ")

            teacher = Teacher(teacher_id, name, subject_taught)
            school.add_teacher(teacher)

            print(f"Teacher {name} added successfully")

        elif choice == "4":
            if not school.courses:
                raise ValueError(
                    "No courses available. Please add a course first."
                    )

            print("\nAvailable Courses:")
            for course in school.courses.values():
                print(f"{course.course_code} - {course.course_title}")

            student_id = input("Enter student ID: ")
            course_code = input("Enter course code: ")

            school.enroll_student(student_id, course_code)

            print(f"Student {student_id} enrolled successfully")
        elif choice == "5":
            school.display_students()

        elif choice == "6":
            school.display_courses_info()

        elif choice == "7":
            student_id = input("Enter student id: ")
            course_code = input("Enter course code: ")

            school.drop_student(student_id, course_code)
            print(f"Student {student_id} droped successfully")

        elif choice == "8":
            school.save_students()
            school.save_courses()
            school.save_teachers()
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please choose from 1 to 8.")
    except ValueError as error:
        print(error)
        school.log_error(str(error))
