'''
Example 12 — Adding, Updating and Removing Set Elements
'''
s = {10, 20, 30}

s.add(40)
print(s)

s.update([50, 60, 70])
print(s)

s.remove(20)
print(s)

s.discard(100)
print(s)

try:
    s.remove(100)
except KeyError:
    print("Element does not exist")

removed = s.pop()
print("Removed:", removed)

s.clear()
print(s)