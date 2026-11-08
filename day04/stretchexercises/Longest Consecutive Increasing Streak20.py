'''
Stretch 20 — Longest Consecutive Increasing Streak
A monitoring system records daily performance values. Find the longest contiguous streak in which each value is strictly greater than the previous one.
'''
performance = [10, 12, 15, 8, 9, 11, 14, 7, 10]

if len(performance) == 0:
    print("No performance data")

else:
    current_length = 1
    max_length = 1

    current_start = 0
    best_start = 0

    for i in range(1, len(performance)):

        if performance[i] > performance[i - 1]:
            current_length += 1

        else:
            current_length = 1
            current_start = i

        if current_length > max_length:
            max_length = current_length
            best_start = current_start

    best_end = best_start + max_length

    print(f"Longest increasing streak = {max_length}")
    print(f"Starting index = {best_start}")
    print(f"Ending index = {best_end - 1}")

    print("Streak values:")

    for i in range(best_start, best_end):
        print(performance[i], end=" ")

    print()