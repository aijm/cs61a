class Account(object):
    """Simple Account class with account_holder, withdraw, deposit"""

    interest = 0.02 # class attribute

    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient funds'
        else:
            self.balance = self.balance - amount
            return self.balance
            


class CheckingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        # return Account.withdraw(self, amount + self.withdraw_fee)
        return super().withdraw(amount + self.withdraw_fee)


class Bank:
    """A bank *has* accounts

    >>> bank = Bank()
    >>> john = bank.open_account('John', 10)
    >>> jack = bank.open_account('Jack', 5, CheckingAccount)
    >>> john.interest
    0.02
    >>> jack.interest
    0.01
    >>> bank.pay_interest()
    >>> john.balance
    10.2
    >>> bank.too_big_to_fail()
    True
    """

    def __init__(self):
        self.accounts = []
    
    def open_account(self, holder, amount, kind=Account):
        account = kind(holder)
        account.deposit(amount)
        self.accounts.append(account)
        return account

    def pay_interest(self):
        for a in self.accounts:
            a.deposit(a.balance * a.interest)

    def too_big_to_fail(self):
        return len(self.accounts) > 1

class A:
    z = -1
    def f(self, x):
        return B(x-1)

class B(A):
    n = 4
    def __init__(self, y):
        if y:
            self.z = self.f(y)
        else:
            self.z = C(y+1)

class C(B):
    """
    >>> a = A()
    >>> b = B(1)
    >>> b.n = 5
    >>> C(2).n
    4
    >>> a.z == C.z
    False
    >>> a.z == b.z
    False
    >>> b.z.z.z
    3
    """
    def f(self, x):
        return x


