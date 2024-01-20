print('<<<   ANALISADOR DE TRIÂNGULO   >>>')
print(' ')
r1 = float(input('Primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos PODEM FORMAR um triângulo.')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo.')
    
