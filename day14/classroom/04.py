'''
Example 04 — UTF-8 Encoding and Unicode
'''

from pathlib import Path

text = "Python — नमस्ते — ಕನ್ನಡ — 日本語"

path = Path("unicode.txt")

path.write_text(text, encoding="utf-8")

data = path.read_bytes()

print("Original:", text)
print("Encoded bytes:", data)
print("Byte length:", len(data))
print("Character length:", len(text))

decoded = data.decode("utf-8")

print("Decoded:", decoded)
print("Same content:", decoded == text)