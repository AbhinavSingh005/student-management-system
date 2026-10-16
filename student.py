students = []

def add_student(roll_no, name, course):
    students.append({
        "roll_no": roll_no,
        "name": name,
        "course": course
    })

def display_students():
    for student in students:
        print(student)

add_student(101, "Rahul", "CSE")
display_students()