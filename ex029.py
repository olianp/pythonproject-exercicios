#Radar eletrônico

n1 = float(input('Informe a velocidade do carro: '))
print('Velocidade máxima da via é 80Km/h.')
multa = (n1-80) * 7
if n1 <= 80:
    print('Você está na velocidade permitida.')
else:
    print('Você ultrapassou em {}Km/h a velocidade permitida.'.format(n1-80))
    print('O valor da sua multa é de R${}.'.format(multa))



    
