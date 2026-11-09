'''
Example 11 — Exception Groups and except*
'''

def validate_records(records):
    errors = []

    for index, record in enumerate(records):
        try:
            age = int(record["age"])

            if age < 0:
                raise ValueError("Negative age")

        except (ValueError, KeyError) as error:
            errors.append(
                ValueError(
                    f"Record {index}: {error}"
                )
            )

    if errors:
        raise ExceptionGroup(
            "Record validation failed",
            errors
        )


records = [
    {"age": "25"},
    {"age": "-5"},
    {"age": "abc"},
    {}
]

try:
    validate_records(records)

except* ValueError as group:
    for error in group.exceptions:
        print(error)