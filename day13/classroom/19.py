'''
Example 19 — Context Manager for Temporary Configuration
'''
from contextlib import contextmanager

settings = {
    "debug": False,
    "timeout": 30
}


@contextmanager
def temporary_setting(key, value):
    old_value = settings[key]
    settings[key] = value

    try:
        yield

    finally:
        settings[key] = old_value


print(settings)

with temporary_setting("debug", True):
    print("Inside:", settings)

print("Outside:", settings)