# Jogo da advinhação
import random

print('O computador está pensando em um número...\nVocê consegue advinhar?')
n1 = int(random.randrange(0,5))
numero = int(input('Digite um número de 0 a 5: '))
print('O número escolhido foi {}.'.format(n1))
if n1 == numero:
    print('Parabéns! Você acertou!')
else:
    print('Não foi dessa vez. Tente novamente!')
print(' ')
print('<<<   FIM DE JOGO   >>>')
