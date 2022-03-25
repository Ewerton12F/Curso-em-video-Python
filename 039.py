#039

from datetime import date

ano = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano

print(f'Quem nasceu em {ano}, tem {idade} em {ano_atual}')

if idade < 18:
  falta = 18 - idade
  print(f'Ainda faltam {falta} anos para o alistamento.\nSeu alistamento será em {falta + ano_atual}')
elif idade > 18:
  atraso = idade - 18
  print(f'Você deveria ter se alistado há {atraso} anos.\nSeu alistamento foi em {ano_atual - atraso}')
elif idade == 18:
  print('Você tem que se alistar IMEDIATAMENTE!')