#079

valor = []

while True:
  x = int(input('Digite um valor: '))

  if x not in valor:
    valor.append(x)
    print('Valor adicionado com sucesso...')
  else:
    print('Valor duplicado! Não vou adicionar...')   

  resp = ' '

  while resp not in 'SsNn':
    resp = input('Quer continuar: [S/N] ').strip()[0]
    if resp in 'Ss':
      continue
    if resp not in 'SsNn':
      print('Informe S ou N!', end = ' ')
  if resp in 'Nn':
    print('Parar!')
    break

print(f'Você digitou os valores {sorted(valor)}')