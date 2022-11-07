company_users = {}
command = input()

while command != "End":
    name, id_num = command.split(" -> ")

    if name not in company_users.keys():
        company_users[name] = [id_num]

    elif name in company_users and id_num not in company_users[name]:
        company_users[name].append(id_num)

    command = input()

for name, id_num in company_users.items():
    print(name)
    print('--', '\n-- '.join(id_num))
