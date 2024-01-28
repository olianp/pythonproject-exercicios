from datetime import date
nasc = int(input('Seu ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('Você tem {} anos.'.format(idade))
if idade < 18:
    print('Ainda falta(m) {} ano(s) para o alistamento militar.'.format(18-idade))
elif idade == 18:
    print('Já está na hora do seu alistamento. Procure a Junta Militar.')
elif idade > 18:
    print('Seu alistamento está há {} ano(s) atrasado. Procure a Junta Militar.'.format(idade-18))
    
    
