#052

num = int(input('Digite um número: '))
tot = 0

for x in range(1, num + 1):
  if num % x == 0:
    print('\033[33m', end=' ')
    tot += 1
  else:
    print('\033[31m', end=' ')
  print(f'{x}', end=' ')
print(f'\n\033[0:0mO número {num} foi divisível por {tot} vezes.')
if tot == 2:
  print('E por isso ele é primo!')