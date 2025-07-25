# project on  Shopping Cart List (Loop + List Interaction)
cart = []
while True:
    item = input("Enter item to add to cart (or 'done' to finish): ")
    if item.lower() == 'done':
        break
    cart.append(item)

print("\n🛒 Your Shopping Cart:")
for index, value in enumerate(cart, 1):
    print(f"{index}. {value}")
