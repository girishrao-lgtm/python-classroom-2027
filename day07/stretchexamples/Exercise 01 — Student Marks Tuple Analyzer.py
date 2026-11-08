'''
Exercise 01 — Student Marks Tuple Analyzer
'''
marks = (78, 45, 90, 32, 67, 88, 40)

total = sum(marks)
average = total / len(marks)
highest = max(marks)
lowest = min(marks)

passing = sum(1 for x in marks if x >= 40)

print(total)
print(f"{average:.2f}")
print(highest)
print(lowest)
print(passing)
