'''
Stretch 15 — Maximum Profit from Stock Prices
'''
prices = [7, 1, 5, 3, 6, 4]

if len(prices) < 2:
    print("Maximum profit: 0")
else:
    minimum = prices[0]
    max_profit = 0

    for price in prices[1:]:

        profit = price - minimum

        max_profit = max(max_profit, profit)

        minimum = min(minimum, price)

    print(f"Maximum profit: {max_profit}")