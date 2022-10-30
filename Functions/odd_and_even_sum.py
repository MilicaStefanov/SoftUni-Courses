def odd_and_even_sum(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0

    for digit in number:
        if int(digit) % 2 == 0:
            sum_of_even_digits += int(digit)
        else:
            sum_of_odd_digits += int(digit)

    return sum_of_odd_digits, sum_of_even_digits


number_as_string = input()
sum_of_odd_digits, sum_of_even_digits = odd_and_even_sum(number_as_string)

print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")
