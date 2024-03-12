nome = str(input('Digite seu nome: '))
gen = str(input('Digite o gênero que você se identifica [M/F]: ')).strip().upper()[0]
while gen not in 'MmFf':
    gen = str(input('OPÇÃO INVÁLIDA! INFORME SEU GÊNERO: ')).strip().upper()[0]
print('Seu nome é {} e você se identifica como {}.'.format(nome, gen))

        

