class Account(object):
    """Simple Account class with account_holder, withdraw, deposit"""
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds')
        else:
            self.balance = self.balance - amount
            

    