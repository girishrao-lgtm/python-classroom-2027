'''
Stretch 08 — Password Attempt Limiter
Allow a maximum of three password attempts. Stop immediately when the correct password is entered.
'''

correct_password = "Python@123"

for attempt in range(1, 4):

    password = input("Enter password: ")

    if password == correct_password:
        print("Access granted")
        break

    print(f"Incorrect password. Attempt {attempt}/3")

else:
    print("Account locked")

    