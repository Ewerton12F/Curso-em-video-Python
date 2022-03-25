#091

from random import randint
from operator import itemgetter

jogada = {}
rankTemp = []
jogo = {}
ranking = {}

print('Valores sorteados:')

for x in range(0, 4):
  jogada[x] = randint(1, 7)
  print(f'Jogador ({x + 1}) tirou {jogada[x]} no dado')
  rankTemp.append(jogada.copy())
  jogada.clear()

print()
print('║' * 31)

for x, y in enumerate(rankTemp):
  for k, v in y.items():
    jogo[k] = v

ranking = sorted(jogo.items() , key=itemgetter(1), reverse = True)

print(f'{"RANKING DOS JOGADORES":^31}')

for i, v in enumerate(ranking):
  print(f'   {i+1}º lugar: Jogador {v[0]+1} com {v[1]}')

print('║' * 31)

#091

from random import randint
from operator import itemgetter

jogos = {'Jogador(1)': randint(1, 6),
         'Jogador(2)': randint(1, 6),
         'Jogador(3)': randint(1, 6),
         'Jogador(4)': randint(1, 6),}
ranking = {}

print('Valores sorteados:')

for x, y in jogos.items():
  print(f'{x} tirou {y}.')

ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
print('◄' * 25)

for x, y in enumerate(ranking):
  print(f'{x+1}º lugar: {y[0]} com {y[1]}')