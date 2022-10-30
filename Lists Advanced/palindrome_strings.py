text = input().split(' ')
palindrome = input()
searched_palindrome = []

for word in text:
    if word == "".join(reversed(word)):
        searched_palindrome.append(word)

print(f'{searched_palindrome}')
print(f'Found palindrome {searched_palindrome.count(palindrome)} times')