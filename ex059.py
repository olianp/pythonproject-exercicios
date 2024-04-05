#Pedir dois valores e decidir operação
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Qual operação você quer realizar? 
      [1] Soma
      [2] Multiplicação
      [3] Maior
      [4] Novos Números
      [5] Sair do Sistema''')
    opcao = int(input('Qual sua opção? '))
    if  opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} é {soma}.')
    elif opcao == 2:
        produto = (valor1 * valor2)
        print(f'O Produto entre {valor1} e {valor2} é {produto}.')
    elif opcao == 3:
        if valor1 < valor2:
            print(f'{valor1} é MENOR que {valor2}.')
        elif valor1 > valor2:
            print(f'{valor1} é MAIOR que {valor2}.')
        else:
            print(f'{valor1} e {valor2} são IGUAIS.')
    elif opcao == 4:
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: ')) 
    elif opcao == 5:
        SystemExit
print('Fim do Programa!')

