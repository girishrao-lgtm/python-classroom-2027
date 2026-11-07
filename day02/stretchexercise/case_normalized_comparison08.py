first = input("Enter first string: ")
second = input("Enter second string: ")

if first.casefold() == second.casefold():
    print("Strings are equal ignoring case")
else:
    print("Strings are different")