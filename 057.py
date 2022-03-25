#057

while True:
  sexo = input('Informe seu sexo: [M/F]: ').strip()[0]
  if sexo in 'MmFf':
    if sexo in 'Mm':
      print('Sexo M registrado com sucesso!')
      break
    else:
      print('Sexo F registrado com sucesso!')
      break
  else:
    print('Informe uma opção válida!')