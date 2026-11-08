'''
Classroom 09 — Remove, Pop, Delete, and Clear
'''
numbers = [10, 20, 30, 20, 40, 50]

numbers.remove(20)
print(f"After remove: {numbers}")

removed = numbers.pop()
print(f"Popped: {removed}")

removed = numbers.pop(1)
print(f"Popped index 1: {removed}")

del numbers[0]
print(f"After del: {numbers}")

numbers.clear()
print(f"After clear: {numbers}")

