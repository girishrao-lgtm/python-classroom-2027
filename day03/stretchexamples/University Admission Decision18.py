'''
University Admission Decision
Difficulty: Hard

A university offers admission based on entrance score and board marks.
- DIRECT ADMISSION: entrance score at least 90 and board marks at least 85
- COUNSELLING: entrance score at least 75 and board marks at least 70
- WAITLIST: entrance score at least 60 and board marks at least 60
- Otherwise: REJECTED
Input: Entrance score and board marks, each from 0–100.

Output: Admission category or INVALID.

'''
entrance = float(input())
board = float(input())

if not (0 <= entrance <= 100 and 0 <= board <= 100):
    print("INVALID")
elif entrance >= 90 and board >= 85:
    print("DIRECT ADMISSION")
elif entrance >= 75 and board >= 70:
    print("COUNSELLING")
elif entrance >= 60 and board >= 60:
    print("WAITLIST")
else:
    print("REJECTED")