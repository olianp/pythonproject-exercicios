# Calculando catetos e hipotenusa

import math
cat1 = float(input('Digite o valor do cateto oposto: '))
cat2 = float(input('Digite o valor do cateto adjacente: '))
# modelo matemático >>> hipo = (cat1 ** 2 + cat2 ** 2) ** 1.5
hipo = math.hypot(cat1, cat2)
print('O valor da hipotenusa é {:.2f}.'.format(hipo))
             
