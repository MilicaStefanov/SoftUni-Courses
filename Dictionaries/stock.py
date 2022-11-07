items = input().split()
searched_items = input().split()
bakery = {}

for index in range(0, len(items), 2):
    key = items[index]
    value = int(items[index + 1])
    bakery[key] = value

for product in searched_items:
    if product in bakery.keys():
        quantity = bakery[product]
        print(f"We have {quantity} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
