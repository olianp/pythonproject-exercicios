somaidade = 0
mediaidade = 0
maiorIdadehomem = 0
maisvelho = ''
totmulher20 = 0
for p in range(1,5):
    print('<<  {}ª pessoa  >>'.format(p))
    nome = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('SEXO [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maiorIdadehomem = Idade
        maisvelho = nome
    if sexo in 'Mm' and idade > maiorIdadehomem:
        maiorIdadehomem = idade
        maisvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1    
mediaidade = somaidade/4
print('A média das idades é {}.'.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}.'.format(maiorIdadehomem, maisvelho))
print('Ao todo, são {} mulheres abaixo dos 20 anos.'.format(totmulher20))



