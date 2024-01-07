#Calcular o dobro, o triplo e raiz quadrada de um número

n1 = float(input('Digite um número: '))
d = n1*2
t = n1*3
rq = n1**1/2
print('O DOBRO de {} é {}, o TRIPLO é {} e a RAIZ QUADRADA é {:.3f}.'.format(n1, d, t, rq))
