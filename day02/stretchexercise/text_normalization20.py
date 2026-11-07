text = input("Enter text: ")

# Step 1: Normalize case
normalized = text.casefold()

# Step 2: Remove selected punctuation
punctuation = ".,!?;:"

for symbol in punctuation:
    normalized = normalized.replace(symbol, "")

# Step 3: Remove extra whitespace
words = normalized.split()

# Step 4: Generate normalized text
cleaned_text = " ".join(words)

# Step 5: Generate slug
slug = "-".join(words)

# Step 6: Count words
word_count = len(words)

print(f"Original: {text}")
print(f"Cleaned: {cleaned_text}")
print(f"Slug: {slug}")
print(f"Word count: {word_count}")