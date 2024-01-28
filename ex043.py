print('<<<   CALCULADORA DE IMC   >>>')
print(' ')
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
print('Seu IMC é: {:.1f}'.format(imc))
print('Situação corporal: ', end='')
if imc < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= imc < 25:
    print('PESO IDEAL')
elif 25 <= imc < 30:
    print('SOBREPESO')
elif 30 <= imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')
    
    
