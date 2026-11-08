'''
Classroom 01 — String creation, identity, and length
Concept: Strings are objects, and len() returns the number of Unicode code points, not the number of bytes.
'''
s1 = "Python"
s2 = 'Python'
s3 = """Python
Deep Dive"""

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")

print(f"Type = {type(s1)}")
print(f"Length of s1 = {len(s1)}")
print(f"Length of s3 = {len(s3)}")

print(f"Object identity = {id(s1)}")
print(f"Memory identity in hex = {hex(id(s1))}")

print(f"Value equality = {s1 == s2}")
print(f"Same object = {s1 is s2}")