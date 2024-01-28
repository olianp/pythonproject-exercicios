n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print('Sua média é {}.'.format(media))
if media < 5:
    print('Você está REPROVADO.')
elif 5 < media < 6.9:
    print('Você está em RECUPERAÇÃO.')
elif media >= 7:
    print('Você está APROVADO.')
    
