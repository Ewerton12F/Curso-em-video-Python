#075

num = (int(input('Digite um valor: ')),
       int(input('Digite outro valor: ')),
       int(input('Digite mais um valor: ')),
       int(input('Digite o último valor: ')))

print('~' * 10)
print('Os números digitados foram:', end = ' ')

nove = par = tres = 0

for x in num:
  print(x, end = ' ')

  if x == 9:
    nove += 1

  if x == 3:
    tres = num.index(3)

  if x % 2 == 0:
    par += 1

print(' ')
print('~' * 10)

print(f'O número 9 apareceu {nove} vezes.')

if tres >= 1:
  print(f'O valor 3 apareceu na posição {tres}.')
else:
  print('Não há número 3.')
  
print(f'Foram digitado {par} vezes números pares.')

print('~' * 10)

print(f'O número 9 apareceu {num.count(9)} vezes.')

if 3 in num:
  print(f'O valor 3 apareceu na {num.index(3) + 1}º posição')
else:
  print('Não há número 3.')