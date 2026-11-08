'''
Classroom 07 — Unicode code points and UTF-8
Concept: Unicode strings versus encoded bytes.
'''
samples = ["A", "é", "अ", "中", "😀"]

for ch in samples:
    encoded = ch.encode("utf-8")

    print(f"Character: {ch}")
    print(f"Code point: U+{ord(ch):04X}")
    print(f"UTF-8 bytes: {encoded}")
    print(f"Character length: {len(ch)}")
    print(f"Byte length: {len(encoded)}")
    print("-" * 30)

text = "नमस्ते"

print(f"String = {text}")
print(f"Code points = {len(text)}")
print(f"UTF-8 bytes = {len(text.encode('utf-8'))}")