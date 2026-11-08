'''
Classroom 18 — Rotate List Right by K Positions
'''
numbers = [10, 20, 30, 40, 50, 60]

k = int(input("Enter rotation count: "))

n = len(numbers)

if n > 0:
    k %= n

    numbers[:] = numbers[-k:] + numbers[:-k] if k else numbers[:]

print(f"Rotated list: {numbers}")
