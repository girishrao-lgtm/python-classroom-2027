text = input("Enter noisy text: ")

cleaned = text.strip()
cleaned = cleaned.strip("#@! ")

print(f"Original: {text!r}")
print(f"Cleaned: {cleaned!r}")