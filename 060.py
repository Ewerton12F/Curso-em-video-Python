#060

num = int(input('Digite um número para calcular o seu fatorial: '))
fat = 1 

print(f'Calculando {num}! =', end=' ')

while num > 0:
  print(num, end='')
  print(' x ' if num > 1 else ' = ', end='')
  fat *= num  
  num -= 1
print(fat)

#060 com for

num = int(input('Digite um número para calcular o seu fatorial: '))
fat = 1

print(f'Calculando {num}! =', end=' ')

for x in range(num, 0, -1): # 1 o valor decrescente que inicia em num está sendo atribuído a x toda vez que ele passa
  print(x, end='')
  print(' x ' if x > 1 else ' = ', end='')
  fat *= x # x irá receber o valor que está sendo contado na linha 1

print(fat)