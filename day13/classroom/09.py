'''
Example 09 — Creating Custom Exceptions
'''
class BankingError(Exception):
    pass


class InsufficientFundsError(BankingError):
    pass


class InvalidAmountError(BankingError):
    pass


class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid amount")

        if amount > self.balance:
            raise InsufficientFundsError(
                "Insufficient funds"
            )

        self.balance -= amount
        return self.balance


account = BankAccount(1000)

for amount in [200, 1500, -50]:
    try:
        print(account.withdraw(amount))

    except BankingError as error:
        print(type(error).__name__, error)