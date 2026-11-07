escaped_path = "C:\new\test"
raw_path = r"C:\new\test"

print("Ordinary string:")
print(escaped_path)

print("Raw string:")
print(raw_path)

print(f"Escaped representation: {escaped_path!r}")
print(f"Raw representation: {raw_path!r}")