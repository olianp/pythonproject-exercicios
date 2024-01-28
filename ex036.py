n1 = float(input('Valor total do imóvel: '))
anos = float(input('Tempo do financiamento em anos: '))
salario = float(input('Valor da sua renda mensal: '))
parcela = n1/(anos*12)
if parcela > (salario*0.3):
    print('EMPRÉSTIMO NÃO APROVADO.')
elif parcela <= (salario*3):
    print('VALOR TOTAL DO IMÓVEL: R${}'.format(n1))
    print('QUANTIDADE DE PARCELAS: R${}'.format(anos*12))
    print('VALOR DA PARCELA: R${:.2f}'.format(parcela))
    
