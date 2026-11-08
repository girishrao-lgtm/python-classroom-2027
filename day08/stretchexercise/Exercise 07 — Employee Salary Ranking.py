'''
Exercise 07 — Employee Salary Ranking
'''
employees = {
    "Amit": 60000,
    "Neha": 85000,
    "Ravi": 60000,
    "Priya": 95000
}

ranking = sorted(
    employees.items(),
    key=lambda item: (-item[1], item[0])
)

for rank, (name, salary) in enumerate(ranking, 1):
    print(rank, name, salary)