'''
Example 08 — Exception Chaining with raise ... from
'''
def load_configuration(value):
    try:
        port = int(value)

    except ValueError as error:
        raise RuntimeError(
            "Configuration contains an invalid port"
        ) from error

    return port


try:
    load_configuration("invalid")

except RuntimeError as error:
    print(error)
    print("Cause:", repr(error.__cause__))