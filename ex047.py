inicio = int(input('Início do intervalo: '))
fim = int(input('Fim do intervalo: '))
print('Os números pares entre {} e {} são: '.format(inicio, fim))
for cont in range(inicio,fim+1,2):
    print(cont)
print('FIM')
