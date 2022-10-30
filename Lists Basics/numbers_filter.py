number_of_lines = int(input())
command_even = "even"
command_odd = "odd"
command_positive = "positive"
command_negative = "negative"

numbers = []

for i in range(number_of_lines):
    current_number = int(input())
    numbers.append(current_number)

command = input()

filtered_numbers = []

for number in numbers:
    filtered_passes = (
        (command == command_even and number % 2 == 0) or
        (command == command_odd and number % 2 != 0) or
        (command == command_negative and number < 0) or
        (command == command_positive and number >= 0)

    )
    if filtered_passes:
        filtered_numbers.append(number)

print(filtered_numbers)







