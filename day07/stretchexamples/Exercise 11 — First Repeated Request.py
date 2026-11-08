'''
Exercise 11 — First Repeated Request
'''
requests = [8, 5, 3, 5, 8, 2, 3]

seen = set()
answer = -1

for request in requests:
    if request in seen:
        answer = request
        break

    seen.add(request)

print(answer)