print('<<<   Reajuste Salarial   >>>')
print(' ')
salario = float(input('Informe seu salário atual: '))
taxa = float(input('Informe a taxa de aumento (%): '))
novosalario = (salario*(taxa/100)+salario)
print('Com aumento de {}%, seu novo salário será de R$ {}.'.format(taxa, novosalario))
