'''
Example 05 — Binary File Operations
'''
from pathlib import Path

source = Path("binary_source.bin")
destination = Path("binary_copy.bin")

data = bytes([0, 1, 2, 100, 200, 255])

source.write_bytes(data)

with source.open("rb") as input_file, destination.open("wb") as output_file:
    while True:
        chunk = input_file.read(4)

        if not chunk:
            break

        output_file.write(chunk)

print(source.read_bytes())
print(destination.read_bytes())

print(
    "Files identical:",
    source.read_bytes() == destination.read_bytes()
)