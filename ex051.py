num = int(input('Digite o primeiro número da sequência: '))
razao = int(input('Digite a razão da sequência: '))
decimo = num + 10 * razao
for c in range (num, decimo, razao):
    print(c, end=' - ')
print('FIM')    
    
