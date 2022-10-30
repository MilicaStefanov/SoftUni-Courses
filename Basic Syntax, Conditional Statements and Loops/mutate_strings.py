word_1 = input()
word_2 = input()
last_printed = word_1

for i in range(0, len(word_1)):
    left_part = word_2[:i + 1]
    right_part = word_1[i + 1:]
    current_string = left_part + right_part

    if current_string == last_printed:
        continue

    print(current_string)

    last_printed = current_string

