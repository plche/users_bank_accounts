class BankAccount:
    all_accounts = []
    def __init__(self, account_type = "Savings", interest_rate = 0, balance = 0):
        self.account_type = account_type
        self.interest_rate = interest_rate / 100
        self.balance = balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdrawal(self, amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient Funds - charging a $5 fee")
            self.balance -= 5
        return self

    def show_account_info(self):
        print(f"Type: {self.account_type}, Balance: ${self.balance}, Interest rate: {self.interest_rate}")
        return self

    def generate_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self
    
    @classmethod
    def print_all_instances(cls):
        for account in cls.all_accounts:
            account.show_account_info()