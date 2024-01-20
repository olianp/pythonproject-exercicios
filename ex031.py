print('<<<   Calculadora Custo de Viagem   >>>')
print(' ')
distancia = float(input('Informe a distância em Km: '))
if distancia <= 200:
    print('O custo do carro para essa distância é de: R${:.2f}.'.format(distancia * 0.5))
else:
    print('O custo do carro para essa distância é de: R${:.2f}.'.format(distancia * 0.45))

print('<<<   TENHA UMA BOA VIAGEM!   >>>')
