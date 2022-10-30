tasks = []

while True:
    command = input()

    if command == "End":
        break

    split_command = command.split("-")
    priority = int(split_command[0])
    current_task = split_command[1]

    tasks.append([priority, current_task])

sorted_tasks = []
for task_data in sorted(tasks):
    sorted_tasks.append(task_data[1])

print(sorted_tasks)