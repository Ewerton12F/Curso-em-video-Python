#045 

from random import randint
from time import sleep

print('''
Suas opções:
| 0 | PEDRA
| 1 | PAPEL
| 2 | TESOURA
''')

jogada = int(input('Qual a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('=-' * 10)
print(f'Computador jogou {itens[computador]}\nJogador jogou {itens[jogada]}')
print('=-' * 10)


if computador == 0:
  if jogada == computador: # pedra = pedra
    print('EMPATE!')
  elif jogada == 1: # pedra < papel
    print('Jogador VENCE!')
  elif jogada == 2: # pedra > tesoura 
    print('Computador VENCE!')
  else:
    print('JOGADA INVÁLIDA!')
elif computador == 1:
  if jogada == 0: # papel > pedra
    print('Computador VENCE!')
  elif jogada == computador: # papel = papel
    print('EMPATE!')
  elif jogada == 2: # papel < tesoura
    print('Jogador VENCE!')
  else:
    print('JOGADA INVÁLIDA!')  
elif computador == 2:
  if jogada == 0: # tesoura > pedra
    print('Jogador VENCE!')
  elif jogada == 1: # tesoura > papel
    print('Computador VENCE!')
  elif jogada == computador: # tesoura = tesoura 
    print('EMPATE!')
  else:
    print('JOGADA INVÁLIDA!')