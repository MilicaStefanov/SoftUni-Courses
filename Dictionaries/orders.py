products_with_prices = {}

while True:
    products = input().split(" ")

    product = products[0]

    if product == "buy":
        break

    price = float(products[1])
    quantity = int(products[2])

    if product not in products_with_prices:
        products_with_prices[product] = [price, quantity]

    elif product in products_with_prices.keys():
        products_with_prices[product][1] += quantity
        if price != products_with_prices[product][0]:
            products_with_prices[product][0] = price

for product, [price, quantity] in products_with_prices.items():
    total_price = price * quantity
    print(f"{product} -> {total_price:.2f}")
