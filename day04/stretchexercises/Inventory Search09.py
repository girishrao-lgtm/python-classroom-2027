'''
Stretch 09 — Inventory Search
Search for a product ID in a list and print its position. If it is not found, display an appropriate message.
'''
products = [101, 205, 309, 412, 518, 620]

target = int(input("Enter product ID: "))

for index in range(len(products)):

    if products[index] == target:
        print(f"Product found at position {index + 1}")
        break

else:
    print("Product not found")
    