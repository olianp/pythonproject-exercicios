print('<<<   CONVERSOR DE TEMPERATURA   >>>')
print(' ')
celsius = float(input('Digite a temperatura em Celsius(°C): '))
kelvin = (celsius+273.15)
fahrenheit = (celsius*1.8+32)
print('Temperatura em Kelvin: {}°K.'.format(kelvin))
print('Temperatura em Fahrenheit: {}°F.'.format(fahrenheit))