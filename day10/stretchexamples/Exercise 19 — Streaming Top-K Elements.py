'''
Exercise 19 — Streaming Top-K Elements
'''
import heapq


def top_k_stream(numbers, k):
    if k <= 0:
        raise ValueError("K must be positive")

    heap = []

    for number in numbers:
        if len(heap) < k:
            heapq.heappush(heap, number)

        elif number > heap[0]:
            heapq.heapreplace(heap, number)

        yield sorted(heap, reverse=True)


numbers = [5, 1, 9, 3, 12, 7, 15, 2]
k = 3

for result in top_k_stream(numbers, k):
    print(result)