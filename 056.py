#056

quantidade = 0
maioridade = 0
midade = 0
hnome = ''

for x in range(0, 4):
  print(f'----- {x + 1}ª PESSOA -----')
  nome = input('Nome: ').strip().capitalize()
  idade = int(input('Idade: '))
  sexo = input('Sexo [M/F]: ').strip().upper()
  print(' ')
  quantidade += idade

  if sexo in 'Mm':
    if maioridade == 0:
      maioridade = idade
    else:
      if idade > maioridade:
        maioridade = idade
        hnome = nome

  if sexo in 'Ff':
    if idade < 20:
      midade += 1

if sexo in 'Mm':
  print(f'A média de idade do grupo é {quantidade / 4:.0f} anos.\nO homem mais velho tem {maioridade} e se chama {hnome}.\nAo todo são {midade} mulher(es) com menos de 20 anos.')
else:
  print(f'A média de idade do grupo é {quantidade / 4:.0f} anos.\nNão há homens.\nAo todo são {midade} mulher(es) com menos de 20 anos.')