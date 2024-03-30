nome = str(input('Digite seu nome: '))
genero = str(input('Digite o gênero que você se identifica [M/F]: ')).strip().upper()[0]
while genero not in 'MmFf':
    genero = str(input('OPÇÃO INVÁLIDA! INFORME SEU GÊNERO: ')).strip().upper()[0]
print(f'Seu nome é {nome} e você se identifica como {genero}.')

        

