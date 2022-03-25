#017

oposto = float(input('Informe o valor do cateto oposto: '))
adjacente = float(input('Informe o valor do cateto adjacente: '))

print(f'A hipotenusa vai medir {(((oposto ** 2) + (adjacente ** 2)) ** (1/2)):.2f}')

#017

import math

oposto = float(input('Informe o valor do cateto oposto: '))
adjacente = float(input('Informe o valor do cateto adjacente: '))

hipotenusa = math.hypot(oposto, adjacente)
print(f'A hipotenusa vai medir: {hipotenusa:.2f}')