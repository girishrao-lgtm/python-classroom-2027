'''
Exercise 03 — Configurable Discount Engine
'''

def discount_engine(percentage):

    def apply_discount(price):
        if price < 0:
            raise ValueError("Invalid price")

        return price * (1 - percentage / 100)

    return apply_discount

student_discount = discount_engine(15)
festival_discount = discount_engine(25)

print(student_discount(2000))
print(festival_discount(2000))