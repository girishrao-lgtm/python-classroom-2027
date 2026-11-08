'''
Example 06 — Variable-Length Keyword Arguments: **kwargs
'''
def employee_profile(**details):
    print("Type:", type(details))

    for key, value in details.items():
        print(key, ":", value)


employee_profile(
    name="Amit",
    department="AI",
    salary=75000
)


def create_record(name, **attributes):
    record = {"name": name}
    record.update(attributes)
    return record


print(create_record("Neha", age=22, city="Bangalore"))