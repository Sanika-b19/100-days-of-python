# Exercise 5: Create a BankAccount Class and Subclasses

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Account Balance: ${self.balance:.2f}")

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance += self.balance * (self.interest_rate / 100)

savings = SavingsAccount("123456", 1000, 1.5)
savings.deposit(500)
savings.apply_interest()
savings.display_balance()  # Output: Account Balance: $1522.50
