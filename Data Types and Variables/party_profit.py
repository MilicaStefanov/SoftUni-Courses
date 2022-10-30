group_size = int(input())
days_of_adventure = int(input())
money = 0

for current_day in range(1, days_of_adventure + 1):
    if current_day % 10 == 0:
        group_size -= 2
    if current_day % 15 == 0:
        group_size += 5
    if current_day % 3 == 0:
        money -= group_size * 3
    if current_day % 5 == 0:
        money += 20 * group_size
        if current_day % 3 == 0:
            money -= 2 * group_size

    money += 50
    money -= 2 * group_size

money_per_companion = int (money // group_size)
print(f"{group_size} companions received {money_per_companion} coins each.")

