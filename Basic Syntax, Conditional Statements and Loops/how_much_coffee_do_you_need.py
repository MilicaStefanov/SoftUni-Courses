command = input()

coffees = 0

command_to_lower = ['coding', 'movie', 'dog', 'cat']
command_to_upper = ['CODING', 'MOVIE', 'DOG', 'CAT']

while command != 'END':

    if command in command_to_lower:
        coffees += 1
    elif command in command_to_upper:
        coffees += 2

    command = input()

    if command == 'END':
        if coffees > 5:
            print('You need extra sleep')
        else:
            print(coffees)