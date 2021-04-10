import bank
import account

class SavingsAccount(account.Account, bank.Bank):
    def __init__(self, code, bank_code, salary):
        super().__init__(code, bank_code)
        self.salary = salary

    def interest_rate(self):
        self._balance *= 1.01
        return self._balance
    
    def mounth_turn(self):
        self.interest_rate()
        self._balance -= self.administration_fee(self._bank_code)
        self.salary += self.salary

class CheckingAccount(account.Account, bank.Bank):
    def __init__(self, code, bank_code, salary):
        super().__init__(code, bank_code)
        self.salary = salary

    def mounth_turn(self):
        self._balance += self.salary
        self._balance -= self.administration_fee(self._bank_code)

    def __str__(self):
        return f"Hi, cliente code: {self.bank_code}! Your current balancy is: {self.account_balance()}"