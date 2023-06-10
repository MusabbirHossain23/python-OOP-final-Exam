from user import User

class Admin:
    def __init__(self, bank):
        self.bank = bank

    def create_account(self, name, email, password):
        user = User(name, email, password)
        self.bank.users.append(user)

    def get_total_balance(self):
        return self.bank.total_balance

    def get_total_loan_amount(self):
        return self.bank.total_loan_amount

    def enable_loan_feature(self):
        self.bank.loan_feature_enabled = True

    def disable_loan_feature(self):
        self.bank.loan_feature_enabled = False
