words = input().split(" ")
my_dictionary = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in my_dictionary:
        my_dictionary[word_lower] = 0
    my_dictionary[word_lower] += 1

for key, value in my_dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
