age = int(input("Enter age: "))
has_id = input("Do you have ID? yes/no: ").lower()

if age < 0:
    print("Invalid age")
elif age >= 18:
    if has_id == "yes":
        print("Entry permitted")
    else:
        print("Valid ID required")
else:
    print("Entry denied: underage")