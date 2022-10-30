number_of_people = int(input())
capacity = int(input())

number_of_times = number_of_people // capacity

if number_of_people % capacity != 0 or number_of_people < capacity:
    number_of_times += 1

if number_of_people == 0:
    number_of_times = 0

print(number_of_times)