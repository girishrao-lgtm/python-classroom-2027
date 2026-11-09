'''
Exercise 05 — Bulk Validation with Exception Groups
'''

class RecordError(Exception):
    pass


def validate_records(records):
    errors = []
    valid = []

    for index, record in enumerate(records):
        try:
            if not isinstance(record, dict):
                raise RecordError("Record must be a dictionary")

            name = record["name"]
            age = record["age"]

            if not isinstance(name, str) or not name.strip():
                raise RecordError("Invalid name")

            if type(age) is not int or age < 0:
                raise RecordError("Invalid age")

            valid.append(record)

        except (KeyError, RecordError) as error:
            errors.append(
                RecordError(f"Record {index}: {error}")
            )

    if errors:
        raise ExceptionGroup("Validation errors", errors)

    return valid


records = [
    {"name": "Alice", "age": 25},
    {"name": "", "age": 30},
    {"name": "Bob", "age": -5},
    {"name": "Charlie", "age": 22}
]

try:
    print(validate_records(records))

except* RecordError as group:
    for error in group.exceptions:
        print(error)
        