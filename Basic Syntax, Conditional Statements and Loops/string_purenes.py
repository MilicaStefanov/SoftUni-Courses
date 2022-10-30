number = int(input())

for i in range(number):
    text = input()
    j = chr(44)
    k = chr(46)
    m = chr(95)

    if text.__contains__(j) or text.__contains__(k) or text.__contains__(m):
        print(f"{text} is not pure!")
    else:
        print(f"{text} is pure.")




