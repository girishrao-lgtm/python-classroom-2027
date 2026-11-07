age = 22
has_ticket = True
is_blocked = False

print(age >= 18 and has_ticket)
print(has_ticket or age >= 18)
print(not is_blocked)

if age >= 18 and has_ticket and not is_blocked:
    print("Entry permitted")
else:
    print("Entry denied")