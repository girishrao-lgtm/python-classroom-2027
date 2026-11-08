'''
Exercise 18 — Top K Frequent Elements
'''

import heapq

numbers = [1, 1, 1, 2, 2, 3, 3, 3, 4]
k = 2

frequency = {}

for x in numbers:
    frequency[x] = frequency.get(x, 0) + 1

heap = []

for number, count in frequency.items():
    heapq.heappush(heap, (-count, number))

result = []

for _ in range(min(k, len(heap))):
    count, number = heapq.heappop(heap)
    result.append(number)

print(result)