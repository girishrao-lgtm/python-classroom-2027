'''
Example 12 — Runtime Polymorphism and Method Overriding
'''

class Payment:

    def pay(self, amount):
        raise NotImplementedError


class CreditCardPayment(Payment):

    def pay(self, amount):
        return f"Credit card payment: {amount}"


class UPIPayment(Payment):

    def pay(self, amount):
        return f"UPI payment: {amount}"


class WalletPayment(Payment):

    def pay(self, amount):
        return f"Wallet payment: {amount}"


payments = [
    CreditCardPayment(),
    UPIPayment(),
    WalletPayment()
]

for payment in payments:
    print(payment.pay(1000))