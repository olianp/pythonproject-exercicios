
# Quebrando um número. Considerar apenas a parte inteira.

import math
num = float(input('Digite um número qualquer: '))
raiz = math.sqrt(num)
print('A raiz de {} é {:.3f}. Sua parte inteira é {}.'.format(num, raiz, math.trunc(raiz)))
          
