from random import randint
from validate_docbr import CPF, CNPJ
import bank
import account
import re
import requests

class Clients(account.Account):
    def __init__(self, code, bank_code, doc, tel, cep):
        super().__init__(code, bank_code)
        doc = str(doc)
        
        if self.check_doc(doc):
            self.doc = doc
        else:
            raise ValueError("Your CPF doesn't match with the CPF pattern")     

        tel = str(tel)
        if self.check_tel(tel):
            self.tel = tel
        else:
            raise ValueError("Your telephone doesn't match with the telephone pattern. Try added you DDD and Country Code!")

        cep = str(cep)
        if self.check_cep(cep):
            self.cep = cep
        else:
            raise ValueError("You cep doesn't match with the cep pattern. A cep have only 8 digits")

    def client_location(self):
        cep_api = f'https://viacep.com.br/ws/{self.cep}/json/'
        cep = requests.get(cep_api)
        cep_r = cep.json()
        return cep_r['uf'], cep_r['localidade'], cep_r['cep']

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

    @staticmethod
    def check_tel(tel):
        client_tel = str(tel)
        client_tel_pattern = re.compile("([0-9]{2,3})?([0-9]{2})?([0-9]{8,9})")
        tel_checked = bool(re.match(client_tel_pattern, client_tel))
        return tel_checked

    @staticmethod
    def check_cep(cep):
        cep = str(cep)
        cep_size = len(cep)
        if cep_size == 8:
            return True
        


    

        
    # def check_cep(self, cep):
    
    #     pass
    # def check_tel(self, tel):
    #     pass
    
x = Clients(6568,237, 11173213988, 48996604747, 88070101)
print(x.cep_txt())