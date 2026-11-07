'''
Login Attempt Validator
Difficulty: Easy+

A login system accepts a user only if the username is student, the password is Python@2027, and the account is not blocked.

Input: Username, password, and blocked status (yes or no) on separate lines.

Output: LOGIN SUCCESS, ACCOUNT BLOCKED, INVALID CREDENTIALS, or INVALID INPUT for an unrecognized blocked status.

'''
username = input()
password = input()
blocked = input().strip().lower()

if blocked not in ("yes", "no"):
    print("INVALID INPUT")
elif blocked == "yes":
    print("ACCOUNT BLOCKED")
elif username == "student" and password == "Python@2027":
    print("LOGIN SUCCESS")
else:
    print("INVALID CREDENTIALS")