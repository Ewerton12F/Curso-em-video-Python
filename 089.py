#089

cadastro = {}
completo = []

while True:
  cadastro['Nome'] = input('Nome: ').strip().capitalize()
  cadastro['Nota1'] = float(input('Nota 1: '))
  cadastro['Nota2'] = float(input('Nota 2: '))
  completo.append(cadastro.copy())
  
  resp = ' '

  while resp not in 'SsNn':
    resp = input('Deseja continuar? [S/N] ')
    if resp in 'Ss':
      continue
    if resp in 'Nn':
      break
    else:
      print('Alternativa inválida!', end = ' ')

  if resp in 'Nn':
    break

print()
print('-=' * 11)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 22)

ind = 1
for x in completo:
  cont = True
  for y, z in x.items():
    if cont == True:
      print(f'{ind:<3} {z:<10} {(x["Nota1"] + x["Nota2"]) / 2:>7.1f}')
    else:
      break
    cont = False
    ind += 1
print()


while True:
  opc = ' '
  opc = input('Mostrar notas de qual aluno? [0 para sair] ').strip().capitalize()

  if opc == '0':
    print('OPÇÃO 0 - SAIR')
    break
  for x in completo:
    cont = True
    for y, z in x.items():
      if cont == True:
        if opc in x['Nome']:
          print(f'1ª Nota: {x["Nota1"]}\n2ª Nota: {x["Nota2"]}')
        else:
          #print('Error!', end = ' ')
          break
      cont = False