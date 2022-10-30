list_of_integer = input().split(" ")
numbers_to_remove = int(input())
second_list = []
third_list = []

for element in list_of_integer:
    element = int(element)
    second_list.append(element)

for number in range(numbers_to_remove):
    second_list.remove(min(second_list))

for element in second_list:
    element = str(element)
    third_list.append(element)

print(", ".join(third_list))