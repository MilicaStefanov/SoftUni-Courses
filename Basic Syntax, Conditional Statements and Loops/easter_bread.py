budget = float(input())
price_for_flour = float(input())
price_for_eggs = price_for_flour * 0.75
price_for_1l_milk = price_for_flour + (price_for_flour * 0.25)
price_for_250ml_milk = price_for_1l_milk / 4
price_for_one_loaf = price_for_flour + price_for_eggs + price_for_250ml_milk
number_of_loaves = 0
colored_eggs = 0

while budget >= price_for_one_loaf:
    budget -= price_for_one_loaf
    number_of_loaves += 1
    colored_eggs += 3

    if number_of_loaves % 3 == 0:
        colored_eggs -= number_of_loaves - 2

print(f"You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")


