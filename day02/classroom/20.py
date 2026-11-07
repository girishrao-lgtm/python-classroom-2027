raw = "   PYTHON,DEEP,DIVE   "

cleaned = raw.strip()
parts = cleaned.split(",")

title = " ".join(parts).title()
slug = "-".join(parts).lower()

print(f"Original: {raw!r}")
print(f"Cleaned: {cleaned}")
print(f"Title: {title}")
print(f"Slug: {slug}")
print(f"Reversed: {title[::-1]}")
print(f"Characters: {len(title)}")