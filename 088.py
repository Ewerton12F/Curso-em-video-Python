#088

from random import randint

jogo = list()
valor = []
num = 0

quant = int(input('Quantos jogos deseja fazer? '))

for y in range(0, quant):
  while len(valor) <= 6:
    num = randint(1, 61)
    if num not in valor and num not in jogo:
      valor.append(num)
  valor.sort()
  jogo.append(valor[:])
  valor.clear()

print('-=' * 3, f'SORTEANDO {quant} JOGOS', '-=' * 3)
for y, x in enumerate(jogo):
  print(f'Jogo {y + 1}: {x}')