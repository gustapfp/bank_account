class Account:
    def __init__(self, code):
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

        