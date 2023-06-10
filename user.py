class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.balance = 0
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance!")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            recipient.deposit(amount)
            self.balance -= amount
            self.transaction_history.append(f"Transferred: {amount} to {recipient.name}")
        else:
            print("Insufficient balance!")

    def get_balance(self):
        return self.balance

    def get_transaction_history(self):
        return self.transaction_history
