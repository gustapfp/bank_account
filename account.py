import bank

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
        return f"Conta de número: {self.code}, saldo: {self.account_balance}, do Banco de código: {self._bank_code}"
    

# x = Account(200, 1)
# print(x)
# x.account_balance = 1000
# y = Account(207)
# y.account_balance = 570
# print(x.account_balance)
# print(y.account_balance)
# x.transfer(300, y)
# print(x.account_balance)
# print(y.account_balance)
# x.deposity(200)
# print(x.account_balance)
# print(y.account_balance)
# y.withdraw(400)
# print(x.account_balance)
# print(y.account_balance)


        