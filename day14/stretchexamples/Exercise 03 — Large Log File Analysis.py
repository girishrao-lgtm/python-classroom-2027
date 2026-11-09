'''
Exercise 03 — Large Log File Analysis
'''

from collections import Counter
from pathlib import Path

path = Path("server.log")

with path.open("w", encoding="utf-8") as file:
    for i in range(10000):
        status = [200, 200, 404, 500][i % 4]
        file.write(f"GET /api/items {status}\n")

status_counts = Counter()
endpoint_counts = Counter()

with path.open("r", encoding="utf-8") as file:
    for line in file:
        parts = line.split()

        if len(parts) != 3:
            continue

        method, endpoint, status = parts

        status_counts[status] += 1
        endpoint_counts[endpoint] += 1

print("Status counts:", status_counts)
print("Endpoint counts:", endpoint_counts)
print("Server errors:", status_counts["500"])

