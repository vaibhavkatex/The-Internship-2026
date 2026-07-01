# Create a class BankAccount with:
# Attributes: account_holder and balance (initialized in __init__).

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

# deposit(amount) — add amount to balance.
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

# withdraw(amount) — subtract amount from balance (only if sufficient
    def withdraw(self, amount):
        if amount <= 0:
            print("Withdraw amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn. New balance: {self.balance}")

# show_balance() — print current balance.
    def show_balance(self):
        print(f"Current balance for {self.account_holder}: {self.balance}")


if __name__ == "__main__":
    # Create an object and demonstrate all methods.
    account = BankAccount("Vaibhav", 1000)
    account.deposit(500)
    account.withdraw(300)
    account.show_balance()

