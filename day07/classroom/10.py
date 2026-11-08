'''
Example 10 — Tuple-Based Student Record Processing
'''
names = ("Amit", "Ravi", "Neha", "Priya")
marks = (85, 72, 95, 88)

records = tuple(zip(names, marks))

for index, (name, mark) in enumerate(records, start=1):
    print(index, name, mark)

topper = max(records, key=lambda x: x[1])
lowest = min(records, key=lambda x: x[1])

print("Topper:", topper)
print("Lowest:", lowest)

average = sum(marks) / len(marks)
print("Average:", average)