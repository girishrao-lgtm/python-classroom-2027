'''
Classroom 08 — Append, Extend, and Insert
'''
numbers = [10, 20, 30]

numbers.append(40)
print(f"After append: {numbers}")

numbers.extend([50, 60])
print(f"After extend: {numbers}")

numbers.insert(1, 15)
print(f"After insert: {numbers}")

numbers.append([70, 80])
print(f"After nested append: {numbers}")

numbers.extend([90, 100])
print(f"After extend: {numbers}")