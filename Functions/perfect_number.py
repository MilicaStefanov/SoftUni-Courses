def is_perfect(some_numbers):
    sum = 0
    for divisor in range(1, some_numbers):
        if some_numbers % divisor == 0:
            sum += divisor
    if sum == some_numbers:
        return "We have a perfect number!"
    return"It's not so perfect."


number = int(input())
print(is_perfect(number))