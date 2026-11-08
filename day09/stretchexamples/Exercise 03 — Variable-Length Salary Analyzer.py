'''
Exercise 03 — Variable-Length Salary Analyzer
'''
def analyze_salaries(*salaries):
    if not salaries:
        return None

    return {
        "count": len(salaries),
        "total": sum(salaries),
        "average": sum(salaries) / len(salaries),
        "highest": max(salaries),
        "lowest": min(salaries)
    }


print(analyze_salaries(40000, 50000, 60000))
print(analyze_salaries(75000))
print(analyze_salaries())