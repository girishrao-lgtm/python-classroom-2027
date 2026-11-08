'''
Example 07 — Combining Parameters, *args and **kwargs
'''

def generate_report(title, *scores, passing_marks=40, **metadata):
    print("Report:", title)
    print("Scores:", scores)

    passed = sum(score >= passing_marks for score in scores)

    print("Passed:", passed)

    for key, value in metadata.items():
        print(key, value)


generate_report(
    "Python Assessment",
    80, 35, 90, 45,
    passing_marks=50,
    batch="2027",
    department="CSE"
)