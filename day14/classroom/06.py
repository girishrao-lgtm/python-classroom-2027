'''
Example 06 — Buffered Reading and Writing
'''

from pathlib import Path

path = Path("buffered_data.bin")

with path.open("wb", buffering=8192) as file:
    for number in range(10000):
        file.write(f"{number}\n".encode())

with path.open("rb", buffering=8192) as file:
    print(file.read(100))

print("File size:", path.stat().st_size)