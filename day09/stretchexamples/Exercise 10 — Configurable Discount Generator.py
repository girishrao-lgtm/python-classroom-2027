'''
Exercise 10 — Configurable Discount Generator
'''
def discount_factory(percentage):
    def apply_discount(price):
        return price * (1 - percentage / 100)

    return apply_discount


student_discount = discount_factory(10)
festival_discount = discount_factory(25)

print(student_discount(2000))
print(festival_discount(2000))
