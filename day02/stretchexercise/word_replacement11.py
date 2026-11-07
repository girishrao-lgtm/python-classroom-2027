text = input("Enter text: ")
old = input("Enter text to replace: ")
new = input("Enter replacement: ")
count = int(input("Enter maximum replacements: "))

if old == "" or count < 0:
    print("Invalid replacement parameters")
else:
    result = text.replace(old, new, count)

    print(f"Original: {text}")
    print(f"Modified: {result}")