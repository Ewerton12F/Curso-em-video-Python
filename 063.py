#063

a = 0
b = 1
c = 0
x = 1

quant = int(input('Quantos termos deseja imprimir: '))

print('~' * (quant * 4))

while x <= quant:

  if quant == 0:
    print('Parar')
    break
  
  print(f'{c}', end=' → ')
  c = a + b
  a = b
  b = c
  c = a

  x += 1
print('FIM')
print('~' * (quant * 4))