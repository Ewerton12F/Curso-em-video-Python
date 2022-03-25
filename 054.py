#054

from datetime import date

quantidade = int(input('Informe a quantidade de pessoas que deseja analisar: '))
maiores = 0 

for x in range(quantidade):
  ano = int(input(f'Em que ano a {x + 1}ª pessoa nasceu? '))
  if date.today().year - ano >= 18:
    maiores += 1 
print(f'Ao todo tivemos {maiores} pessoas maiores de idade.\nE também tivemos {quantidade - maiores} pessoas menores de idade.')