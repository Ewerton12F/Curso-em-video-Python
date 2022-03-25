#098

def func(ini, fim, pas):
  print('-=' * 15)
  print(f'Contagem de {ini} até {fim} de {pas} em {pas}')
  for x in range(ini, fim + 1, pas):
    print(x, end = ' ')
  print('FIM!')
  

print(func(1, 10, 1))
print(func(10, 0, -1))

print('-=' * 15)
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))

print(func(ini, fim, pas))

#098 USANDO WHILE

from time import sleep

def func(i, f, p):
  if p < 0:
    p *= -1
  if p == 0:
    p = 1
  print('-=' * 15)
  print(f'Contagem de {i} até {f} de {p} em {p}')

  if i < f:
    count = i
    while count <= f:
      print(f'{count}', end = ' ')
      sleep(0.5)
      count += p
    print('FIM!')
  else:
    count = i
    while count >= f:
      print(f'{count}', end = ' ')
      sleep(0.5)
      count -= p
    print('FIM!')

print(func(1, 10, 1))
print(func(10, 0, 2))

print('-=' * 15)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

print(func(i, f, p))