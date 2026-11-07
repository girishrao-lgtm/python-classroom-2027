'''

API Rate Limit Decision
Difficulty: Medium+

An API permits at most 100 requests per minute for free users and 1,000 for premium users. A blocked account is always denied.

Input: Plan (free or premium), requests already made, blocked status (yes/no) on separate lines.

Output: ALLOW, RATE LIMIT EXCEEDED, ACCOUNT BLOCKED, or INVALID INPUT.
'''
plan = input().strip().lower()
requests = int(input())
blocked = input().strip().lower()

if (
    plan not in ("free", "premium")
    or requests < 0
    or blocked not in ("yes", "no")
):
    print("INVALID INPUT")
elif blocked == "yes":
    print("ACCOUNT BLOCKED")
else:
    limit = 100 if plan == "free" else 1000

    if requests + 1 > limit:
        print("RATE LIMIT EXCEEDED")
    else:
        print("ALLOW")