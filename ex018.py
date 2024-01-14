import math

print('<<<   Calculadora de Seno, Cosseno e Tangente   >>>')
print(' ')
angulo = float(input('Digite o valor do ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do seno: {:.3f}.'.format(seno))
print('O valor do Cosseno: {:.3f}.'.format(cosseno))
print('O valor da Tangente: {:.3f}.'.format(tangente))

