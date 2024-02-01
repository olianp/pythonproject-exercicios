from datetime import date
ano = date.today().year
maior = 0
menor = 0
for c in range(1,8):
    nasc = int(input('Digite o {}º ano de nascimento: '.format(c)))
    idade = ano - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('{} pessoas são menores de idade e {} são maiores de idade.'.format(menor, maior))
