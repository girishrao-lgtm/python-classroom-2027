'''
Exercise 11 — Independent Request Counters
'''

def create_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


api_a = create_counter()
api_b = create_counter()

print(api_a())
print(api_a())
print(api_b())
print(api_a())
print(api_b())

