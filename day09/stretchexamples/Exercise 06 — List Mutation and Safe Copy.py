'''
Exercise 06 — List Mutation and Safe Copy
'''

def unsafe_update(values, item):
    values.append(item)
    return values


def safe_update(values, item):
    copied = values.copy()
    copied.append(item)
    return copied


original = [10, 20, 30]

result1 = unsafe_update(original, 40)

print("Original after unsafe:", original)
print("Result:", result1)

result2 = safe_update(original, 50)

print("Original after safe:", original)
print("Result:", result2)