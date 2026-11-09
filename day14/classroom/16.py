'''
Example 16 — Gzip Compression
'''
import gzip
from pathlib import Path

source = Path("application.log")

source.write_text(
    "INFO Application started\n" * 1000,
    encoding="utf-8"
)

compressed = Path("application.log.gz")

with source.open("rb") as input_file, gzip.open(compressed, "wb") as output_file:
    while chunk := input_file.read(8192):
        output_file.write(chunk)

with gzip.open(compressed, "rt", encoding="utf-8") as file:
    content = file.read()

print("Original size:", source.stat().st_size)
print("Compressed size:", compressed.stat().st_size)
print("Restored correctly:", content == source.read_text(encoding="utf-8"))