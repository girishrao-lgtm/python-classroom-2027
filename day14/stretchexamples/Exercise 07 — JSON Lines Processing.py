'''
Exercise 07 — JSON Lines Processing
'''

import json
from pathlib import Path

path = Path("events.jsonl")

events = [
    {"event": "login", "user": "Alice"},
    {"event": "purchase", "user": "Bob"},
    {"event": "login", "user": "Charlie"},
    {"event": "logout", "user": "Alice"}
]

with path.open("w", encoding="utf-8") as file:
    for event in events:
        file.write(json.dumps(event) + "\n")

counts = {}

with path.open("r", encoding="utf-8") as file:
    for line in file:
        event = json.loads(line)

        name = event["event"]

        counts[name] = counts.get(name, 0) + 1

print(counts)