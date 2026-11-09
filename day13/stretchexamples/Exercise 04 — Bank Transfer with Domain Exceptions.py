'''
Exercise 04 — Bank Transfer with Domain Exceptions
'''
class BankingError(Exception):
    pass


class InsufficientFundsError(BankingError):
    pass


class InvalidTransferError(BankingError):
    pass


class Account:

    def __init__(self, account_id, balance):
        self.account_id = account_id
        self.balance = balance


def transfer(source, destination, amount):
    if amount <= 0:
        raise InvalidTransferError("Invalid transfer amount")

    if source is destination:
        raise InvalidTransferError("Same source and destination")

    if source.balance < amount:
        raise InsufficientFundsError("Insufficient funds")

    source.balance -= amount
    destination.balance += amount


account1 = Account("A101", 5000)
account2 = Account("A102", 2000)

try:
    transfer(account1, account2, 1500)

except BankingError as error:
    print(error)

print(account1.balance)
print(account2.balance)