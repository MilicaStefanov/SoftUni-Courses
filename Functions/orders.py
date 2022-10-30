def price(current_product, quantity):
    if current_product == "coffee":
        return 1.50 * quantity
    elif current_product == "water":
        return 1.00 * quantity
    elif current_product == "coke":
        return 1.40 * quantity
    elif current_product == "snacks":
        return 2.00 * quantity


product = input()
quantity_of_products = int(input())

result = price(product, quantity_of_products)

print(f'{result:.2f}')

