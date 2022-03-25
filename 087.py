#086 e #087

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]] 
spar = maior = scol = 0

for x in range(0, 3):
  for y in range(0, 3):
    matriz[x][y] = int(input(f'Informe um valor para [{x}, {y}]: '))
print('~-' * 30)
for x in range(0, 3):
  for y in range(0, 3):
    print(f'[{matriz[x][y]:^5}]', end = ' ')
    if matriz[x][y] % 2 == 0:
      spar += matriz[x][y]
  print()

print('~-' * 30)

print(f'A soma de todos os números pares é {spar}.')

for x in range(0, 3):
  scol += matriz[x][2]
print(f'A soma de todos os números da terceira coluna é {scol}.')

for y in range(0, 3):
  if y == 0:
    maior = matriz[1][y]
  elif matriz[1][y] > maior:
    maior = matriz[1][y] 
print(f'O maior valor da segunda linha é {maior}.')