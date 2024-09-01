# Exercise 5: Bank Account Class

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.__account_holder = account_holder  # Private attribute
        self.__balance = balance  # Private attribute

   def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid deposit amount.")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance is {self.__balance}.")
        else:
            print("Invalid or insufficient funds for withdrawal.")

    def get_balance(self):
        return self.__balance

account = BankAccount("John Doe", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Final balance: {account.get_balance()}")
