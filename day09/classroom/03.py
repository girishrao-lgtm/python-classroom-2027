'''
Example 03 — Default Parameters and Argument Binding
'''

def calculate_bill(price, quantity=1, discount=0):
    total = price * quantity
    return total - total * discount / 100


print(calculate_bill(1000))
print(calculate_bill(1000, 3))
print(calculate_bill(1000, 3, 10))
print(calculate_bill(1000, discount=20))


def display(a, b=10, c=20):
    print(a, b, c)


display(5)
display(5, c=50)
display(5, 15, 25)
