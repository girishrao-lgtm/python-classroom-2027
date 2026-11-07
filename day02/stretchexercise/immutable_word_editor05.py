word = input("Enter word: ")
replacement = input("Enter replacement character: ")

if word and len(replacement) == 1:
    modified = replacement + word[1:]

    print(f"Original: {word}")
    print(f"Modified: {modified}")
else:
    print("Invalid input")