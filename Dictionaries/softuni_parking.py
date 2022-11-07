number = int(input())
parking = {}

for num in range(number):
    command = input().split(" ")

    action = command[0]

    if action == "register":
        username = command[1]
        license_plate_number = command[2]

        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        username = command[1]

        if username not in parking.keys():
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking[username]

for usernames, license_plate_numbers in parking.items():
    print(f"{usernames} => {license_plate_numbers}")
