#082

L = list()
par = []
impar = []

while True:
  L.append(int(input('Digite um número: ')))

  resp = ' '

  while resp not in 'SsNn':
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Ss':
      continue
  if resp in 'Nn':
    print('~' * 20)
    break

for y, x in enumerate(L):
  if x % 2 == 0:
    par.append(x)
  else:
    impar.append(x)

print('A lista completa é', L)
print('A lista de pares é', par)
print('A lista de ímpares é', impar)