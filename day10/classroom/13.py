'''
Example 13 — Generator throw(), close() and Cleanup
'''

def controlled_generator():
    try:
        number = 1

        while True:
            try:
                yield number
                number += 1

            except ValueError:
                print("ValueError handled inside generator")

    finally:
        print("Generator cleanup executed")


generator = controlled_generator()

print(next(generator))
print(next(generator))

print(generator.throw(ValueError("Reset signal")))

print(next(generator))

generator.close()

print("Closed")

