'''
Example 08 — Dictionary Traversal Patterns
'''
marks = {
    "Amit": 85,
    "Neha": 95,
    "Ravi": 72,
    "Priya": 88
}

for name, value in marks.items():
    print(name, value)

for name, score in marks.items():
    print(name, score)

for score in marks.values():
    print(score)

for index, (name, score) in enumerate(marks.items(), 1):
    print(index, name, score)