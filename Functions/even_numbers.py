def check_even_numbers(even_num):
    if int(even_num) % 2 == 0:
        return True
    return False


number = [int(even_num) for even_num in input().split()]
sorted_numbers = []
even_numbers_iterator = filter(check_even_numbers, number)
even_numbers = list(even_numbers_iterator)

print(even_numbers)

