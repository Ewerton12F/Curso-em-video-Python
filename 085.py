#085

L = [[], []]
valor = 0

for x in range(0, 6):
  valor = int(input('Informe um valor: '))
  if valor % 2 == 0:
    L[0].append(valor)
  else:
    L[1].append(valor)

L[0].sort()
print(L[0])
L[1].sort()
print(L[1])