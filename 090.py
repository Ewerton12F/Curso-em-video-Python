#090

ficha = {}

while True:
  ficha['nome'] = input('Infome o nome do aluno: ').capitalize()
  ficha['media'] = float(input(f'Informe a média de {ficha["nome"]}: '))
  ficha['situ'] = 'Aprovado!' if ficha['media'] >= 7 else 'Reprovado!'
  print()
  print('█' * 30)
  print()

  for x, y in ficha.items():
    if x == 'nome':
      print('O nome é', y)
    elif x == 'media':
      print('A média é', y)
    elif x == 'situ':
      print('A situação é:', y)
  break