number = int(input())
students = {}

for num in range(number):
    name = input()
    grade = float(input())

    if name not in students:
        students[name] = grade

    else:
        list_averages = [students[name], grade]
        students[name] = list_averages


for name, grade in students.items():
    if type(grade) == list:
        average_grade = sum(grade) / len(grade)
    else:
        average_grade = grade

    if average_grade >= 4.5:
        print(f'{name} -> {average_grade:.2f}')
