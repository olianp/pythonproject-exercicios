from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-='*11)
print('Computador escolheu {}.'.format(itens[computador]))
print('Jogador escolheu {}.'.format(itens[jogador]))
print('-='*11)
if computador == 0:
    if jogador == 0:
        print('COMPUTADOR E JOGADOR EMPATARAM.')
    elif jogador == 1: 
        print('JOGADOR GANHOU.')
    elif jogador == 2:
        print ('COMPUTADOR GANHOU.')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR GANHOU.')
    elif jogador == 1:
        print('COMPUTADOR E JOGADOR EMPATARAM.')
    elif jogador == 2:
        print('JOGADOR GANHOU.')
elif computador == 2:
    if jogador == 0:
        print('JOGADOR GANHOU.')
    elif jogador == 1:
        print('COMPUTADOR GANHOU.')
    elif jogador == 2:
        print('COMPUTADOR E JOGADOR EMPATARAM.')
        
