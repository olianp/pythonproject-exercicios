#Calculando aumento de salário

salario = float(input('Informe o seu salário: '))
if salario <= 1250:
    aumento = (salario * 0.15) + salario
    print('Você recebeu um aumento de 15%. Seu novo salário é de R${}.'.format(aumento))
else:
    aumento = (salario * 0.10) + salario
    print('Você recebeu um aumento de 10%. Seu novo salário é de R${}.'.format(aumento))

