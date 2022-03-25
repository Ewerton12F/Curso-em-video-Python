#041

from datetime import date

ano = int(input('Informe a data de nascimento: '))

idade = date.today().year - ano

print(f'O atleta tem {idade} anos.')

if idade > 25:
  print('Classificação: MASTER')
elif idade <= 25:
  print('Classificação: SENIOR')
elif idade <= 19:
  print('Classificação: JUNIOR')
elif idade <= 14:
  print('Classificação: INFANTIL')
elif idade <= 9:
  print('Classificação: MIRIM')