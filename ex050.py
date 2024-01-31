soma = 0
cont = 0
for c in range (1,6):
    num = int(input('Digite o {} valor: '.format(c)))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('A soma dos {} valores pares é: {}.'.format(cont,soma))
    
