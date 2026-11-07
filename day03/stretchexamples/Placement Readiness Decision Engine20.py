'''
Placement Readiness Decision Engine
Difficulty: Hard

A placement preparation platform classifies students using CGPA, coding score, aptitude score, communication score, and active backlogs.

Apply the following rules in order:
1. Any active backlog: NOT ELIGIBLE
2. CGPA below 7.0: ACADEMIC IMPROVEMENT
3. Coding score below 60: CODING IMPROVEMENT
4. Aptitude score below 60: APTITUDE IMPROVEMENT
5. Communication score below 50: COMMUNICATION IMPROVEMENT
6. If coding, aptitude, and communication scores are all at least 85: HIGH PRIORITY PLACEMENT
7. Otherwise: PLACEMENT READY
Input: CGPA, coding score, aptitude score, communication score, and active backlogs on separate lines.

Output: Exactly one classification, or INVALID INPUT for values outside their valid ranges.

Constraint: CGPA is 0–10, scores are 0–100, and backlogs are nonnegative.

'''
cgpa = float(input())
coding = int(input())
aptitude = int(input())
communication = int(input())
backlogs = int(input())

if not (
    0 <= cgpa <= 10
    and 0 <= coding <= 100
    and 0 <= aptitude <= 100
    and 0 <= communication <= 100
    and backlogs >= 0
):
    print("INVALID INPUT")
elif backlogs > 0:
    print("NOT ELIGIBLE")
elif cgpa < 7.0:
    print("ACADEMIC IMPROVEMENT")
elif coding < 60:
    print("CODING IMPROVEMENT")
elif aptitude < 60:
    print("APTITUDE IMPROVEMENT")
elif communication < 50:
    print("COMMUNICATION IMPROVEMENT")
elif (
    coding >= 85
    and aptitude >= 85
    and communication >= 85
):
    print("HIGH PRIORITY PLACEMENT")
else:
    print("PLACEMENT READY")