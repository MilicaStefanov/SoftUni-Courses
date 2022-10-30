factor_number = int(input())
count_number = int(input())
number_list = []

for element in range(1, count_number + 1):
    number_list.append(factor_number * element)

print(number_list)
