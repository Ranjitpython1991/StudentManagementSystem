class Student:
    def __init__(self, student_id, name, age, grade):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.grade = grade
        self.courses = []  # list of enrolled courses

    def enroll_course(self, course):
        if course not in self.courses:
            self.courses.append(course)


class Course:
    def __init__(self, course_id, course_name, credits):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.students = []  # list of enrolled students

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)


class StudentManagementSystem:
    def __init__(self):
        self.students = {}  # {id: Student}
        self.courses = {}   # {id: Course}

    def add_student(self, student_id, name, age, grade):
        if student_id not in self.students:
            self.students[student_id] = Student(student_id, name, age, grade)

    def add_course(self, course_id, course_name, credits):
        if course_id not in self.courses:
            self.courses[course_id] = Course(course_id, course_name, credits)

    def enroll(self, student_id, course_id):
        if student_id in self.students and course_id in self.courses:
            student = self.students[student_id]
            course = self.courses[course_id]
            student.enroll_course(course)
            course.add_student(student)
