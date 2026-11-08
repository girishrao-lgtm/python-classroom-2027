'''
Exercise 09 — Access Control Validation
'''
required_permissions = {"read", "write"}

users = {
    "Amit": {"read", "write", "execute"},
    "Neha": {"read"},
    "Ravi": {"read", "write"},
    "Priya": {"write", "execute"}
}

for name, permissions in users.items():
    if required_permissions <= permissions:
        print(name, "ACCESS GRANTED")
    else:
        print(name, "ACCESS DENIED")