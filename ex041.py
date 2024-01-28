from datetime import date
print('<<<   CAMPEONATO DE NATAÇÃO   >>>')
print(' ')
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você tem {} anos.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM.')
elif 10 < idade <= 14:
    print('Sua categoria é INFANTIL.')
elif 15 < idade <= 19:
    print('Sua categoria é JÚNIOR.')
elif 20 < idade <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
    
