title = input("Enter title: ")

words = title.strip().lower().split()

slug = "-".join(words)

print(f"Slug: {slug}")