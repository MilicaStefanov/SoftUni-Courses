number = int(input())
word = input()
string = []

for _ in range(number):
    current_word = input()
    string.append(current_word)

print(string)

for i in range(len(string) -1, -1, -1):
    element = string[i]
    if word not in element:
        string.remove(element)

print(string)