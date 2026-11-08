'''
Exercise 20 — Large Log Processing Pipeline
'''
def read_logs():
    logs = [
        "INFO|2026-11-01|User login",
        "ERROR|2026-11-01|Database timeout",
        "WARNING|2026-11-02|High memory usage",
        "ERROR|2026-11-02|Connection failed",
        "INFO|2026-11-03|Request completed",
        "ERROR|2026-11-03|Disk unavailable"
    ]

    yield from logs


def parse_logs(lines):
    for line in lines:
        parts = line.split("|", 2)

        if len(parts) != 3:
            continue

        level, date, message = parts

        yield {
            "level": level,
            "date": date,
            "message": message
        }


def filter_errors(records):
    for record in records:
        if record["level"] == "ERROR":
            yield record


def group_by_date(records):
    counts = {}

    for record in records:
        date = record["date"]
        counts[date] = counts.get(date, 0) + 1

    return counts


pipeline = filter_errors(
    parse_logs(
        read_logs()
    )
)

result = group_by_date(pipeline)

for date, count in sorted(result.items()):
    print(date, count)
