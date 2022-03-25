#081

L = list()

while True:
  L.append(int(input('Digite um valor: ')))

  resp = input('Quer continuar? [S/N]').strip()[0]

  while resp not in 'SsNn':
    
    if resp in 'Ss':
      continue
  if resp in 'Nn':
    break

print(f'Você digitou {len(L)} elementos.')
L.sort(reverse = True)
print(f'Os valores em ordem decrescente são {L}')
print(f'O valor 5 faz parte da lista!' if 5 in L else 'O valor 5 não faz parte da lista.')