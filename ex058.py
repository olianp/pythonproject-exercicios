#Jogo da Advinhação 2.0
import random
print('Qual número o computador está pensando?')
n1=int(random.randrange(0,10))
acerto = False
cont = 0
while not acerto:
    aposta = int(input('Faça sua aposta entre 0 e 10: '))
    cont += 1
    if aposta < n1:
            print('Você errou para menos! Tente novamente.')
    elif aposta > n1:
            print('Você errou para mais. Tente novamente.')
    else:
            aposta == n1
            acerto = True
            print(f'Você acertou depois de {cont} tentativas. Parabéns!')


