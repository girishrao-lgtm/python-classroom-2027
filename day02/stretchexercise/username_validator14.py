username = input("Enter username: ")

valid_length = 5 <= len(username) <= 15
valid_characters = username.isalnum()

if valid_length and valid_characters:
    print("Valid username")
else:
    print("Invalid username")