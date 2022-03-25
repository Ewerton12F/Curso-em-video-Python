#078

a = list()
maior = posmaior = menor = posmenor = 0

for x in range(0, 5):
  a.append(int(input(f'Informe um valor na posição {x + 1}: ')))
  if x == 0:
    maior = menor = a[x]
  else:
    if a[x] > maior:
      maior = a[x]
      posmaior = x + 1
    if a[x] < menor:
      menor = a[x]
      posmenor = x + 1

print('-=' * 20)

print(f'O menor valor foi {menor} nas posições ', end = '')
for i, v in enumerate(a):
  if v == menor:
    print(f'{i + 1}...', end = ' ')

print()

print(f'O maior valor foi {maior} nas posições ', end = '')
for i, v in enumerate(a):
  if v == maior:
    print(f'{i + 1}...', end = ' ')

#078

valores = []

for i in range(0,5):
  valores.append(eval(input('Digite um valor para a lista: ')))

print(f'O valor maior é {max(valores)} e fica na posição {valores.index(max(valores))}')

print(f'O valor menor é {min(valores)} e fica na posição {valores.index(min(valores))}')