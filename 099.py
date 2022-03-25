#099 - USANDO FOR E LISTA

def maior(L):
  m = 0
  for x in range(0, len(L)):
    if L[x] > m:
      m = L[x]
  print(f'O maior é {m}')

maior([2, 9, 4, 5, 7, 1])
maior([4, 7, 0])
maior([1, 2])
maior([6])

#099 - USANDO DESEMPACOTADOR

def maior(* num):
  m = 0
  for x, y in enumerate(num):
    if x == 0:
      m = y
    else:
      if m < y:
        m = y
  print(m)

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)