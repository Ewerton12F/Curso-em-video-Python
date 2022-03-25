#094

cadastro = {}
ficha = []
soma = media = 0

while True:
  cadastro.clear()
  cadastro['Nome'] = input('Nome: ').capitalize()

  while True:
    cadastro['Sexo'] = input('Sexo: [M/F] ').upper().strip()[0]
    if cadastro['Sexo'] in 'MF':
      break
    print('Alternativa inválida!', end=' ')

  cadastro['Idade'] = int(input('Informe a idade: '))
  soma += cadastro['Idade']
  
  ficha.append(cadastro.copy())
  
  resp = ' '
  while resp not in 'SNsn':
    resp = input('Deseja continuar? [S/N] ')
    if resp not in 'SNsn':
      print('Alternativa inválida!', end=' ')
  if resp in 'Nn':
    break

print('╔' * 40)

print(f'A) Ao todo foram cadastradas {len(ficha)} pessoas')

media = soma / len(ficha)
print(f'B) A média de idade é {media:5.2f} anos.')

print('C) As mulher(es) cadastradas foi/foram:', end = ' ')
for x in ficha:
  if x['Sexo'] in 'F':
    print(f'{x["Nome"]}', end = ' ')
print()

print('D) As pessoas com idade acima da média foram:')
for x in ficha:
  if x['Idade'] > media:
    print('    ', end = '')
    for y, z in x.items():
      print(f'{y} = {z}; ', end = '')
print()
print('Encerrado!')