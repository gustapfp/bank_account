import bank
import account

class SavingsAccount(account.Account, bank.Bank):
    def __init__(self, code, bank_code):
        super().__init__(code, bank_code)

    def interest_rate(self):
        self._balance *= 1.01
        return self._balance
    
    def mounth_turn(self):
        self.interest_rate()
        self._balance -= self.administration_fee(self._bank_code)

class CheckingAccount(account.Account, bank.Bank):
    def __init__(self, code, bank_code):
        super().__init__(code, bank_code)

    def mounth_turn(self):
        self._balance -= self.administration_fee(self._bank_code)
    
    

x = SavingsAccount(1, 237)
x.account_balance = 1000
x.mounth_turn()
print(x)

x.mounth_turn()
print(x)

x.mounth_turn()
print(x)

x.mounth_turn()
print(x)