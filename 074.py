#074

from random import randint

cpu = (randint(1, 10), randint(1, 10), randint(1, 10),
       randint(1, 10), randint(1, 10))
y = 0

for x in cpu:
  print(x, end = ' ')

  y += 1

  if y == 1:
    maior = menor = x
  else:
    if x > maior:
      maior = x
    if x < menor:
      menor = x

print('')
print('~0' * 10)
print(maior)
print(menor)

print(max(cpu))
print(min(cpu))