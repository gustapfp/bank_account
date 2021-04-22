import bank
import account
import account_types as at
from random import randint
from operator import attrgetter


chico = at.SavingsAccount(6568, 237, randint(0,1000), 11173213988, 48996604747, 88070101)
rebecca = at.SavingsAccount(3384, 341, randint(0,1000), 18405125710, 59487801696, '51310090') 
gustavo = at.SavingsAccount(5886, 104, randint(0,1000), '04180203960', 87722470828, 67125128)  
julia = at.SavingsAccount(7869, 237, randint(0,1000), 15134928371, 5544828223369, 58106155)
saulo = at.CheckingAccount(5789, 260, randint(0,1000), 90921919220, 10120498104765, 78010020)
marcia = at.CheckingAccount(3618, 341, randint(0,1000), 68630301872, '0156534349615', 81050657)
bar_joao = at.CheckingAccount(6710, 77, randint(0,1000),'02006762442492', 89161808397, 82515290) 
lanchonete_que_fome = at.CheckingAccount(6842, 104, randint(0,1000), 94731827238280, 73205780132, 75064865)
livraria_leia_aqui = at.CheckingAccount(8641, 260, randint(0,10000), 76444962292046, 513634158, 79075114)

clients = [
    chico,
    rebecca,
    gustavo, 
    julia,
    saulo, 
    marcia, 
    bar_joao, 
    lanchonete_que_fome, 
    livraria_leia_aqui
]

months = 0
while months != 120:
    for i in range(len(clients)):
        clients[i].mounth_turn()
    months +=1

clients =  sorted(clients, key=attrgetter('_balance'), reverse=True)
for i in range(len(clients)):
    print(clients[i])