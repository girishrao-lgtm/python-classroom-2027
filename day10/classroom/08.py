'''
Example 08 — Generator State and Local Variables
'''

def running_total():
    total = 0

    for number in [10, 20, 30, 40]:
        total += number
        yield total


generator = running_total()

print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

print("Generator state:", generator.gi_frame is None)