'''
Example 16 — Sorting Dictionaries
'''
marks = {
    "Amit": 85,
    "Neha": 95,
    "Ravi": 72,
    "Priya": 88
}

by_name = dict(sorted(marks.items()))
print(by_name)

by_marks = dict(
    sorted(marks.items(), key=lambda item: item[1])
)

print(by_marks)

ranked = sorted(
    marks.items(),
    key=lambda item: (-item[1], item[0])
)

print(ranked)