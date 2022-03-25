#068

from random import randint

player = 0
pc = 0

print('==' * 10)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('==' * 10)

while True:
  num = int(input('Diga o valor: '))
  opc = ' '
  com = randint(1, 10)

  while opc not in 'PpIi':
    opc = input('Par ou Ímpar? [P/I] ').strip().upper()[0]
  print(f'Você jogou {num} e o computador, {com}. Total de {num + com}', end=' ')
  print('~' * 10)
  print(f'DEU PAR!' if (num + com) % 2 == 0 else 'DEU ÍMPAR!')
  print('-=' * 10)
  if opc == 'P':
    if (com + num) % 2 == 0:
      print('MIZERAVI!')
      print('-=' * 10)
      player += 1
    else:
      print(f'Poxa mizeravi :/')
      print('-=' * 10)
      pc += 1
      if player > pc:
        print(f'GANHOU! Você venceu {player} vezes.')
      else:
        print(f'PERDEU! Você venceu {player} vezes, mas o computador venceu {pc}.')
      break
  else:
    if (com + num) % 2 != 0:
      print('MIZERAVI!')
      print('-=' * 10)
      player += 1
    else:
      print(f':/')
      print('-=' * 10)
      if player > pc:
        print(f'GANHOU! Você venceu {player} vezes.')
      else:
        print(f'PERDEU! Você venceu {player} vezes, mas o computador venceu {pc}.')
      pc += 1
      break