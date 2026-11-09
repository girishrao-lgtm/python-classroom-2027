'''
Exercise 10 — Compressed JSON Backup
'''

import gzip
import json
from pathlib import Path

records = [
    {"id": i, "status": "ACTIVE"}
    for i in range(10000)
]

backup = Path("backup.json.gz")

with gzip.open(backup, "wt", encoding="utf-8") as file:
    json.dump(records, file)

with gzip.open(backup, "rt", encoding="utf-8") as file:
    restored = json.load(file)

print("Records restored:", len(restored))
print("Data identical:", restored == records)
print("Backup size:", backup.stat().st_size)