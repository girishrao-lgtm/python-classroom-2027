'''
Example 01 — Functions Are First-Class Objects
'''

def greet(name):
    return f"Hello, {name}"

message = greet

print(greet("Alice"))
print(message("Bob"))

print(greet is message)
print(type(greet))