#048

s = 0
contador = 0

for x in range(1, 501, 2):
  if x % 3 == 0:
    s += x
    contador += 1
print(f'A soma de todos os {contador} valores solicitados é {s}')