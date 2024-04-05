# Cálculo de Fatorial - por módulo
# from math import factorial
# n = int(input('Digite um número: '))
# fatorial = factorial(n)
# print(f'O fatorial de {n}! é: {fatorial}')

# Cálculo Fatorial - modo tradicional
print('<<< Calculadora de Fatorial >>>')
print(' ')
n = int(input('Digite um número: '))
c = n
fatorial = 1
print(f'Calculando {c}! = ', end='')
while c > 0:
   print(f'{c}', end='') 
   print(' x ' if c > 1 else ' = ', end='')
   fatorial *= c
   c-=1
print(f'{fatorial}')