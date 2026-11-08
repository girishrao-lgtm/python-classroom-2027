'''
Stretch 03 — Inventory Stock Update
'''
stock = [100, 200, 150, 300, 250]

index = int(input("Enter product index (0-4): "))
change = int(input("Enter stock change: "))

if 0 <= index < len(stock):

    if stock[index] + change < 0:
        print("Insufficient stock")
    else:
        stock[index] += change
        print(f"Updated stock: {stock}")

else:
    print("Invalid product index")