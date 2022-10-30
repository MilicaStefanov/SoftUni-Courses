deck_of_cards = input().split(" ")
faro_shuffles = int(input())

for shuffle in range(faro_shuffles):
    final_deck = []
    middle_of_the_deck = len(deck_of_cards) // 2
    left_part = deck_of_cards[0:middle_of_the_deck]
    right_part = deck_of_cards[middle_of_the_deck::]

    for car_index in range(len(left_part)):
        final_deck.append(left_part[car_index])
        final_deck.append(right_part[car_index])

    deck_of_cards = final_deck

print(deck_of_cards)
