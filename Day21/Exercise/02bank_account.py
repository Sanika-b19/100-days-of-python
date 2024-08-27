# Exercise 2: Create a Bank Account Class

class BankAccount:
    def __init__(self, account_number, owner_name, balance=0):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def check_balance(self):
        return self.balance

account = BankAccount("123456", "Jane Doe", 1000)
account.deposit(500)
account.withdraw(200)
print(f"Balance: {account.check_balance()}")  # Output: Balance: 1300
