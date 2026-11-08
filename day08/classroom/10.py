'''
Example 10 — Deep Copy and Nested Mutable Objects
'''

import copy

original = {
    "student": "Amit",
    "scores": {
        "Python": [80, 90],
        "Java": [75, 85]
    }
}

shallow = original.copy()
deep = copy.deepcopy(original)

shallow["scores"]["Python"].append(100)
deep["scores"]["Java"].append(95)

print("Original:", original)
print("Shallow:", shallow)
print("Deep:", deep)