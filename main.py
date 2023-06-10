from bank import Bank
from user import User
from admin import Admin

# Example Usage:

bank = Bank()
admin = Admin(bank)

admin.create_account("Musabbir", "musabbir@example.com", "password1")
admin.create_account("Hossain", "Hossain@example.com", "password2")
admin.create_account("Admin", "admin@example.com", "adminpass")

admin.disable_loan_feature()

user1 = bank.get_user("musabbir@example.com")
user2 = bank.get_user("Hossain@example.com")

user1.deposit(2000)
user1.withdraw(300)
user1.transfer(user2, 500)
user2.withdraw(4000)
print(user1.get_balance())  # Output: 300
print(user2.get_balance())  # Output: 200
print(user1.get_transaction_history())  # Output: ['Deposited: 1000', 'Withdrawn: 500', 'Transferred: 200 to Hossain']
print(user2.get_transaction_history())  # Output: ['Deposited: 200', 'Withdrawn: 1000']

print(admin.get_total_balance())  # Output: 0
print(admin.get_total_loan_amount())  # Output: 0
