print('Gerador de P.A. V3.0')
print('='*30)
primeiro = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais   
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razão
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM')
print(f'Progressão realizada com {total} termos mostrados.')   
