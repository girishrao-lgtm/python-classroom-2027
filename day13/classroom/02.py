'''
Example 02 — Basic try and except
'''
values = ["10", "20", "abc", "40"]

for value in values:
    try:
        number = int(value)
        print(number * 2)

    except ValueError:
        print(f"Invalid integer: {value}")