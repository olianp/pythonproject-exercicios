print('Gerador de P.A.')
print('-'*30)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <=10:
    print(f'{termo} -> ', end='')
    termo += razão
    cont += 1
print('FIM')

