number_of_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_value = 0

for current_snowball in range(number_of_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())

    snowball_value = (snowball_weight / snowball_time) ** snowball_quality

    if snowball_value > max_value:
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality
        max_value = snowball_value

print(f"{max_weight} : {max_time} = {int(max_value)} ({max_quality})")
