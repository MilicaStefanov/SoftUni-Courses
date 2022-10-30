divisor = int(input())
boundary = int(input())
num = 0

for i in range(1, boundary + 1):
    if i % divisor == 0:
        if i <= boundary:
            if i != 0:
                num = i
print(num)