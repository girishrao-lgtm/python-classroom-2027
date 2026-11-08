'''
Stretch 18 — Maximum Sum of K Consecutive Days
'''
sales = [100, 200, 300, 150, 400, 250, 500]

k = int(input("Enter window size: "))

n = len(sales)

if k <= 0 or k > n:
    print("Invalid window size")
else:
    window_sum = sum(sales[:k])
    max_sum = window_sum
    best_start = 0

    for i in range(k, n):

        window_sum += sales[i]
        window_sum -= sales[i - k]

        if window_sum > max_sum:
            max_sum = window_sum
            best_start = i - k + 1

    print(f"Maximum sales: {max_sum}")
    print(f"Best window: {sales[best_start:best_start + k]}")
    