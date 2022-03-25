#092

from datetime import datetime

cadastro = {}
form = []

cadastro['Nome'] = input('Nome: ')
nasc = int(input('Ano de nascimento: '))
cadastro['Idade'] = datetime.now().year - nasc
cadastro['CTPS'] = int(input('Nº da CTPS: '))
if cadastro['CTPS'] != 0:
  cadastro['Contratação'] = int(input('Ano de contratação: '))
  cadastro['Salário'] = float(input('Salário: '))
  cadastro['Aposentadoria'] = cadastro['Idade'] + ((cadastro['Contratação'] + 35) - datetime.now().year)
form.append(cadastro.copy())
  
print()
print('☼' * 40)
print()

for y, z in cadastro.items():
  print(f'► A chave {y} tem valor: {z}')