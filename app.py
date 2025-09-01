from flask import Flask, render_template, request, redirect, url_for
from student_model import StudentManagementSystem

app = Flask(__name__)
sms = StudentManagementSystem()

@app.route('/')
def index():
    return render_template('index.html')

# ----- Students -----
@app.route('/students')
def students():
    return render_template('students.html', students=sms.students.values())

@app.route('/add_student', methods=['POST'])
def add_student():
    student_id = request.form.get('student_id')
    name = request.form.get('name')
    age = request.form.get('age')
    grade = request.form.get('grade')
    if student_id and name:
        sms.add_student(student_id, name, age, grade)
    return redirect(url_for('students'))

# ----- Courses -----
@app.route('/courses')
def courses():
    return render_template('courses.html', courses=sms.courses.values())

@app.route('/add_course', methods=['POST'])
def add_course():
    course_id = request.form.get('course_id')
    course_name = request.form.get('course_name')
    credits = request.form.get('credits')
    if course_id and course_name:
        sms.add_course(course_id, course_name, credits)
    return redirect(url_for('courses'))

# ----- Enroll -----
@app.route('/enroll', methods=['GET', 'POST'])
def enroll():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        course_id = request.form.get('course_id')

        if not student_id or not course_id:
            return "❌ Missing student or course selection!", 400

        sms.enroll(student_id, course_id)
        return redirect(url_for('index'))

    return render_template(
        'enroll.html',
        students=sms.students.values(),
        courses=sms.courses.values()
    )

if __name__ == '__main__':
    app.run(debug=True)
