#084

temp = []
princ = []
maiorp = menorp = 0

while True:
  temp.append(input('Informe o nome da pessoa: '))
  temp.append(float(input('Informe o peso da pessoa: ')))

  if len(princ) == 0:
    maiorp = menorp = temp[1]

  else:
    if temp[1] > maiorp:
      maiorp = temp[1]
    if temp[1] < menorp:
      menorp = temp[1]
      
  princ.append(temp[:])
  temp.clear()
  
  resp = ' '

  while resp not in 'SsNn':
    resp = input('Deseja continuar [S/N]: ').strip()[0]
    if resp in 'Ss':
      continue
    elif resp in 'Nn':
      print('Parou')
      break
    else:
      print('Alternativa inválida.', end = ' ')
  if resp in 'Nn':
    print('Parou aqui também')
    break

print(f'Foram cadastradas {len(princ)} pessoas.')
print(f'O maior peso foi {maiorp}kg. Peso de ', end = '')
for p in princ:
  if p[1] == maiorp:
    print(f'{p[0]}')
print(f'O menor peso foi {menorp}kg. Peso de ', end = '')
for p in princ:
  if p[1] == menorp:
    print(f'{p[0]}')