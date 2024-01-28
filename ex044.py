print('<<<   GERENCIADOR DE PAGAMENTOS    >>>')
print(' ')
valor = float(input('Valor da compra: '))
print('''FORMA DE PAGAMENTO
[1] à vista/chque
[2] à vista no cartão
[3] 2x sem juros 
[4] 3x ou mais com juros''')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    preco = valor - (valor * 0.10)
    print('DESCONTO: {:.2f}'.format(valor*0.10))
    print('TOTAL DA COMPRA: {:.2f}'.format(preco))
elif opcao == 2:
    preco = valor - (valor * 0.05)
    print('DESCONTO: {:.2f}'.format(valor*0.05))
    print('TOTAL DA COMPRA: {:.2f}'.format(preco))
elif opcao == 3:
    parcela = (valor / 2)
    print('VALOR DA PARCELA: {:.2f}'.format(parcela))
    print('TOTAL DA COMPRA: {:.2f}'.format(valor))
elif opcao == 4:
    preco = valor + (valor * 0.20)
    parcela = int(input('Número de parcelas: '))
    print('ACRÉSCIMO: {:.2f}'.format(valor*0.20))
    print('TOTAL DA COMPRA : {:.2f}'.format(preco))
    print('VALOR DA PARCELA: {:.2f}'.format(preco/parcela))
else:
    print('OPÇÃO INVÁLIDA!')
    
