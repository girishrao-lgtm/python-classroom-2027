text = input("Enter multilingual text: ")

encoded = text.encode("utf-8")

print(f"Text: {text}")
print(f"Code points: {len(text)}")
print(f"UTF-8 bytes: {len(encoded)}")
print(f"Encoded data: {encoded}")