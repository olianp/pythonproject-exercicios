print('<<<   TABUADA   >>>')
print(' ')
num = int(input('Você quer a tabuada de qual número? '))
for c in range(0,11):
    print('{} x {} = {}.'.format(num, c, num*c))
print(' ')
print('<<<   FIM   >>>')
