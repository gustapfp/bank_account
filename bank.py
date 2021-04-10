class Bank:
    def __init__(self, bank_code):
       if self.check_bank_code(bank_code) == True:
           self._bank_code = bank_code
       else:
           raise LookupError("This bank is not registered on our system!")

    @staticmethod
    def check_bank_code(bank_code):
        registered_banks = [('Banco do Brasil', 1), ('Bradesco', 237), ('Nubank', 260), ('Itau', 341), ('Banco Inter', 77), ('Caixa', 104)]
                
        for code in range(len(registered_banks)):
            if bank_code == registered_banks[code][1]:
                print(f"welcome to bank: {registered_banks[code][0]}!")
                return True
        return False

    def administration_fee(self, bank_code):
        banks_fee = {
            1:22.90,
            237:25.90, 
            260:0,
            341:33.00,
            77:0, 
            104:21
        }
        return banks_fee[bank_code]