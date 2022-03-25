#049

numero = int(input('Digite um número para ver sua tabuada: '))

for x in range(1, 11):
  print(f'{numero} x {x:2.0f} = {numero * x}')