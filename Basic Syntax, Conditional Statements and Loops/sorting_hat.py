name = input()
j = 0

while name != "Welcome!":

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    for i in range(len(name)):

        j = len(name)

    if j < 5:
        print(f'{name} goes to Gryffindor.')
    elif j == 5:
        print(f"{name} goes to Slytherin.")
    elif j == 6:
        print(f"{name} goes to Ravenclaw.")
    elif j > 6:
        print(f"{name} goes to Hufflepuff.")

    name = input()

    if name == "Welcome!":
        print("Welcome to Hogwarts.")