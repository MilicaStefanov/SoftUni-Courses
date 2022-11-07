courses = {}
command = input()

while command != "end":
    course_name, student_name = command.split(" : ")

    if course_name not in courses.keys():
        courses[course_name] = [student_name]

    elif course_name in courses:
        courses[course_name].append(student_name)

    command = input()

for course, students in courses.items():
    print(f"{course}: {len(students)}")
    print('--', '\n-- '.join(students))
