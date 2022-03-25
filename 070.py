#070

mprec = cont = bprec = totmil = totprec = 0

print('-' * 26)
print('    LOJA SUPER BARATÃO')
print('-' * 26)

while True:
  prod = input('Nome do produto: ').strip().capitalize()
  prec = int(input('Preço: R$'))

  totprec += prec
  cont += 1

  if prec >= 1000:
    totmil += 1
  if cont == 1 or prec < bprec:
    bprec = prec
    bprod = prod
  
  esc = ' '
  while esc not in 'SsNn':
    print('~' * 25)
    esc = input('Quer continuar? [S/N] ').strip()[0]

    if esc in 'Ss':
      print('~' * 25)
    if esc not in 'SsNn':
      print('')
      print('○' * 23)
      print('       É S ou N')
      print('○' * 23)
      print('')

  if esc in 'Nn':
      print('------- FIM DO PROGRAMA -------')
      break

print(f'O total da compra foi de R${totprec:.2f}')
print(f'Temos {totmil} produto(s) custando mais de R$1000')
print(f'O produto mais barato foi {bprod} que custa R${bprec:.2f}')