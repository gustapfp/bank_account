from random import randint
from validate_docbr import CPF, CNPJ
import bank
import account
import re

class Clients(account.Account):
    def __init__(self, code, bank_code, doc, tel): #, cep):
        super().__init__(code, bank_code)
        self.tel = tel
        # self.cep = cep
        doc = str(doc)

        if self.check_doc(doc):
            self.doc = doc
        else:
            raise ValueError("Your CPF doen't match with the CPF pattern")     

    @staticmethod
    def check_doc(doc):
        client_doc = str(doc)
        client_doc_size = len(client_doc)

        if client_doc_size == 11:
            cpf = CPF()
            return cpf.validate(doc)
        
        elif client_doc_size == 14:
            cnpj = CNPJ()
            return cnpj.validate(doc)
        
        else:
            return False

    
    def check_tel(self, tel):
        client_tel = str(self.tel)
        client_tel_pattern = re.compile("([0-9]{2,3})?([0-9]{2})?([0-9]{8,9})")
        tel_cheked = bool(re.match(client_tel_pattern, client_tel))
        return tel_cheked
        


    

        
    # def check_cep(self, cep):
    
    #     pass
    # def check_tel(self, tel):
    #     pass
    
x = Clients(6568,237, 11173213988, 48996604747)
print(x.check_tel(48996604747))