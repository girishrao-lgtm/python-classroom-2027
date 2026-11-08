'''
Exercise 02 — Bank Account Using Closures
'''
def create_account(initial_balance):

    balance = initial_balance

    def deposit(amount):
        nonlocal balance

        if amount <= 0:
            raise ValueError("Invalid deposit")

        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance

        if amount <= 0 or amount > balance:
            raise ValueError("Invalid withdrawal")

        balance -= amount
        return balance

    def get_balance():
        return balance

    return deposit, withdraw, get_balance

deposit, withdraw, balance = create_account(5000)

print(deposit(2000))
print(withdraw(1500))
print(balance())
