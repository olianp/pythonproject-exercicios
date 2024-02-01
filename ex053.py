frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
#inverso = junto[::-1] -> pode ser feito dessa forma também, sem o laço.
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(inverso)
if inverso == junto
    print('Essa frase É UM PALÍNDROMO.')
else:
    print('Essa frase NÃO É UM PALÍNDROMO.')
