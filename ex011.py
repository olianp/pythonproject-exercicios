print('<<< Calculadora de Tinta >>>')
print(' ')
largura = float(input('Informe a largura em metros(m): '))
altura = float(input('Informe a altura em metros: '))
tinta = (largura*altura)/2
print('A área tem {} m². É necessário {} litros de tinta para pintá-la.'.format((largura*altura), tinta))
