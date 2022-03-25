#028

from random import randint
from time import sleep

computador = randint(1, 5)

print('\033[1;31m-=-' * 18)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
print('\033[1;31m-=-' * 18)

num = int(input('Em que número eu pensei? '))

print('\033[1;31mPROCESSANDO...')
sleep(1)
print('\033[1;31mPARABENS! Você acertou!' if num == computador else f'Você errou! O número pensado foi {computador} e não {num}')