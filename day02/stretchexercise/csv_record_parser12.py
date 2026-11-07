record = input("Enter name,roll,marks: ")

fields = record.split(",")

if len(fields) != 3:
    print("Invalid record format")
else:
    name = fields[0].strip()
    roll = fields[1].strip()
    marks_text = fields[2].strip()

    try:
        marks = float(marks_text)

        if name and roll and 0 <= marks <= 100:
            print(f"Name: {name}")
            print(f"Roll: {roll}")
            print(f"Marks: {marks:.2f}")
        else:
            print("Invalid record values")

    except ValueError:
        print("Marks must be numeric")