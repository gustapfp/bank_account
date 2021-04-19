import bank
import account
import account_types as at
from random import randint
from operator import attrgetter



chico = at.SavingsAccount(6568,237,  randint(0,1000))
rebecca = at.SavingsAccount(3384, 341, randint(0,1000)) 
gustavo = at.SavingsAccount(5886, 104, randint(0,1000))  
julia = at.SavingsAccount(7869, 237, randint(0,1000))
saulo = at.CheckingAccount(5789, 260, randint(0,1000))
marcia = at.CheckingAccount(3618, 341, randint(0,1000))
everaldo = at.CheckingAccount(6710, 77, randint(0,1000)) 
fernanda = at.CheckingAccount(6842, 104, randint(0,1000))
koda = at.CheckingAccount(8641, 260, randint(0,10000))

clients = [
    chico,
    rebecca,
    gustavo, 
    julia,
    saulo, 
    marcia, 
    everaldo, 
    fernanda, 
    koda
]

months = 0
while months != 120:
    for i in range(len(clients)):
        clients[i].mounth_turn()
    months +=1

clients =  sorted(clients, key=attrgetter('_balance'), reverse=True)
for i in range(len(clients)):
    print(clients[i])