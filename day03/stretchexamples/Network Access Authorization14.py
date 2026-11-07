'''
Network Access Authorization
Difficulty: Medium+

A service grants access only if a user is authenticated, the account is active, and the user has the required role (admin or developer). Maintenance mode blocks developers but permits administrators.

Input: Authenticated (yes/no), active (yes/no), role, and maintenance (yes/no) on separate lines.

Output: ACCESS GRANTED, ACCESS DENIED, or INVALID INPUT for an unrecognized Boolean response.

'''
authenticated = input().strip().lower()
active = input().strip().lower()
role = input().strip().lower()
maintenance = input().strip().lower()

if (
    authenticated not in ("yes", "no")
    or active not in ("yes", "no")
    or maintenance not in ("yes", "no")
):
    print("INVALID INPUT")
elif (
    authenticated == "yes"
    and active == "yes"
    and role in ("admin", "developer")
    and (maintenance == "no" or role == "admin")
):
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")