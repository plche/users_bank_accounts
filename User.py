from BankAccount import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.savings_bank_account = BankAccount()
        self.checking_bank_account = BankAccount("Checking")
    def make_deposit(self, account_type, amount):
        if self.checking_bank_account.account_type == account_type:
            self.checking_bank_account.balance += amount
        else:
            self.savings_bank_account.balance += amount
        return self
    def make_withdrawal(self, account_type, amount):
        if self.checking_bank_account.account_type == account_type:
            self.checking_bank_account.balance -= amount
        else:
            self.savings_bank_account.balance -= amount
        return self
    def show_bank_account_balance(self, account_type):
        if self.checking_bank_account.account_type == account_type:
            print(f"User: {self.name}, Type: {self.checking_bank_account.account_type}, Balance: ${self.checking_bank_account.balance}")
        else:
            print(f"User: {self.name}, Type: {self.savings_bank_account.account_type}, Balance: ${self.savings_bank_account.balance}")
        return self
    def make_transfer(self, user, account_type, amount):
        user.make_deposit(account_type, amount)
        self.make_withdrawal(account_type, amount)
        return self