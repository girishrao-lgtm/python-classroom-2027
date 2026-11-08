'''
Exercise 02 — Bank Account with Transaction History
'''

from decimal import Decimal


class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = Decimal(str(balance))
        self._transactions = []

        if self._balance < 0:
            raise ValueError("Invalid opening balance")

    @property
    def balance(self):
        return self._balance

    @property
    def transactions(self):
        return tuple(self._transactions)

    def deposit(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0:
            raise ValueError("Invalid deposit")

        self._balance += amount
        self._transactions.append(("DEPOSIT", amount))

    def withdraw(self, amount):
        amount = Decimal(str(amount))

        if amount <= 0 or amount > self._balance:
            raise ValueError("Invalid withdrawal")

        self._balance -= amount
        self._transactions.append(("WITHDRAW", amount))


account = BankAccount("ACC101", "5000.00")

account.deposit("2000.00")
account.withdraw("1500.00")

print(account.balance)
print(account.transactions)