'''
Student Scholarship Eligibility
Difficulty: Easy

A student qualifies for a scholarship if CGPA is at least 8.5, attendance is at least 85%, and active backlogs are zero.

Input: cgpa attendance backlogs as three values on separate lines.

Output: ELIGIBLE, NOT ELIGIBLE, or INVALID for CGPA outside 0–10, attendance outside 0–100, or negative backlogs.
Input (CGPA, attendance, backlogs)	Output
9.0, 90, 0	ELIGIBLE
8.5, 85, 0	ELIGIBLE
8.4, 95, 0	NOT ELIGIBLE
9.0, 84, 0	NOT ELIGIBLE
9.0, 90, 1	NOT ELIGIBLE
11, 90, 0	INVALID
'''
cgpa = float(input())
attendance = float(input())
backlogs = int(input())

if not (0 <= cgpa <= 10 and 0 <= attendance <= 100 and backlogs >= 0):
    print("INVALID")
elif cgpa >= 8.5 and attendance >= 85 and backlogs == 0:
    print("ELIGIBLE")
else:
    print("NOT ELIGIBLE")