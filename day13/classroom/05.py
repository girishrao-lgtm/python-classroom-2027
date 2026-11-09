'''
Example 05 — Exception Propagation Through the Call Stack
'''
def level_three():
    return 10 / 0


def level_two():
    return level_three()


def level_one():
    return level_two()


try:
    level_one()

except ZeroDivisionError as error:
    print("Exception caught at top level")
    print(type(error).__name__)
    print(error)
    