'''
Stretch 07 — Unicode Text Inspector
Inspect a user-entered string and display each code point and its UTF-8 byte length.
'''
text = input("Enter Unicode text: ")

total_bytes = 0

for index, ch in enumerate(text):

    encoded = ch.encode("utf-8")
    byte_count = len(encoded)

    total_bytes += byte_count

    print(f"Index: {index}")
    print(f"Character: {ch}")
    print(f"Unicode: U+{ord(ch):04X}")
    print(f"UTF-8 bytes: {byte_count}")
    print("-" * 25)

print(f"Total code points = {len(text)}")
print(f"Total UTF-8 bytes = {total_bytes}")