print('<<<   CALCULADORA DE DESCONTO   >>>')
print(' ')
preco = float(input('Digite o preço regular do produto: '))
taxa = float(input('Taxa de desconto que deseja aplicar (%): '))
novopreco = float((preco*(taxa/100))-preco)
print('O valor do produto com {}% de desconto é: {:.2f}.'.format(taxa, novopreco))
