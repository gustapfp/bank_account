import bank
from functools import total_ordering

@total_ordering
class Account(bank.Bank):
    def __init__(self, code, bank_code):
        super().__init__(bank_code)
        self.code = code
        self._balance = 0
    @property
    def account_balance(self): 
        return self._balance
         
    @account_balance.setter
    def account_balance(self, money_value):
        self._balance = money_value

    def transfer(self, money_value, other_account):
        self._balance -= money_value
        other_account._balance += money_value

    def deposity(self, money_value):
        self._balance += money_value

    def withdraw(self, money_value):
        self._balance -= money_value

    def __str__(self):
        return f"Account number: {self.code}, balance: {self.account_balance}, bank code: {self._bank_code}"

    def __eq__(self, other_balance):
        accountA = self.account_balance() 
        accountB = self.account_balance()
        return accountA == accountB
    
    def __lt__(self, other_balance):
        accountA = self.account_balance() 
        accountB = self.account_balance()
        return accountA < accountB