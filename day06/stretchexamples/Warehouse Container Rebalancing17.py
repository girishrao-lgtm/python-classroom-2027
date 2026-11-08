'''
Stretch 17 — Warehouse Container Rebalancing
'''
containers = [10, 20, 30, 40, 50]

total = sum(containers)
n = len(containers)

if n == 0:
    print("No containers")
else:
    target = total // n
    remainder = total % n

    balanced = [target] * n

    for i in range(remainder):
        balanced[i] += 1

    movements = 0

    for i in range(n):
        if containers[i] > balanced[i]:
            movements += containers[i] - balanced[i]

    print(f"Balanced containers: {balanced}")
    print(f"Units moved: {movements}")