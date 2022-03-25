#018

from math import radians, sin, tan, cos
ang = float(input('Digite o valor do ângulo: '))
seno = sin(radians(ang))
print(f'O ângulo de {ang} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ang))
print(f'O ângulo de {ang} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ang))
print(f'O ângulo de {ang} tem a TANGENTE de {tangente:.2f}')