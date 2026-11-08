'''
Example 03 — Instance Methods and self
'''
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
            return

        self.balance -= amount

    def display(self):
        print(self.account_number, self.balance)


account = BankAccount("ACC101", 5000)

account.deposit(2000)
account.withdraw(1500)
account.display()

BankAccount.deposit(account, 500)

account.display()