'''
Example 17 — itertools.groupby() and Consecutive Grouping
'''
from itertools import groupby

data = [
    ("CSE", "Amit"),
    ("CSE", "Ravi"),
    ("AI", "Neha"),
    ("AI", "Priya"),
    ("CSE", "Karan")
]

data.sort(key=lambda item: item[0])

for department, group in groupby(data, key=lambda item: item[0]):
    names = [name for _, name in group]
    print(department, names)

    