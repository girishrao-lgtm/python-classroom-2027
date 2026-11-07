text = input("Enter text: ")

for character in text:
    print(
        f"Character: {character!r}, "
        f"Code point: U+{ord(character):04X}"
    )