def collected_character(first, second):
    character = []
    for current_character in range(ord(first) + 1, ord(second)):
        character.append(chr(current_character))
    return character


first_character = input()
second_character = input()
result = collected_character(first_character, second_character)

print(' '.join(result))
