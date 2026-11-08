'''
Stretch 11 — Product Price Increase
'''
prices = [100, 250, 500, 750, 1000]

percentage = float(input("Increase percentage: "))

for i in range(len(prices)):
    prices[i] += prices[i] * percentage / 100

print(f"Updated prices: {prices}")