'''
Example 04 — Closures and Captured Variables
'''
def multiplier(factor):

    def multiply(number):
        return number * factor

    return multiply

double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))

print(double.__closure__)

for cell in double.__closure__:
    print(cell.cell_contents)
    