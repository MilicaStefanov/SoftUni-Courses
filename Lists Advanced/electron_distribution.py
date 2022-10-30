number_of_electrons = int(input())
filled_shells = []
n = 1

while 0 < number_of_electrons:
    shell = 2 * (n ** 2)

    if number_of_electrons >= shell:
        filled_shells.append(shell)
        number_of_electrons -= shell
    else:
        filled_shells.append(number_of_electrons)
        number_of_electrons -= shell

    n += 1

print(filled_shells)