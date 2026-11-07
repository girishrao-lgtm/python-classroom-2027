filename = input("Enter filename: ")

normalized = filename.strip().lower()

if normalized.endswith((".py", ".java", ".cpp")):
    print("Supported source file")
else:
    print("Unsupported source file")