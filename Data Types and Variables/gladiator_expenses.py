lost_fights_count = int(input())
helmet_price = int(input())
sword_price = int(input())
armor_price = int(input())
helmet_count = 0

for current_fight in range(lost_fights_count):

    if lost_fights_count % 2 == 0:
        helmet_count += 1
        helmet_price = helmet_price * helmet_count
