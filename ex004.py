#Dissecando uma variável

algo = input('Digite algo: ')
print('O tipo primitivo é: ', (type(algo)))
print('É apenas numérico? ', (algo.isnumeric()))
print('É apenas alfabético?', (algo.isalpha()))
print('É alfanumérico?', (algo.isalnum()))
print('Possui todas as letras minúsculas?', (algo.islower()))
print('Possui todas as letras maiúsculas?', (algo.isupper()))

