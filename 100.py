#100

from random import randint

def sorteia(L):
  for x in range(0, 5):
    L.append(randint(0, 10))
  for x in L:
    print(x, end = ' ')
  print()

def par(L):
  par = 0
  for x in L:
    if x % 2 == 0:
      par += x
  print(par)


L = []
sorteia(L)
par(L)