#069

adult = 0
homem = 0
mulher = 0

print('-' * 27)
print('    CADASTRE UMA PESSOA')
print('-' * 27)

while True:
  idade = int(input('Idade: '))
  if idade >= 18:
    adult += 1
  
  sexo = ' '
  while sexo not in 'MmFf':
    sexo = input('Sexo: [M/F] ').strip()[0]
    if sexo in 'Ff' and idade < 20:
      mulher += 1
    elif sexo in 'Mm':
      homem += 1
  
  cont = ' '
  while cont not in 'SsNn':
    cont = input('Quer continuar? [S/N] ').strip()[0]
    print('~' * 25)
  if cont in 'Nn':
    break

print('=-' * 21)
print('Total de pessoas com mais de 18 anos:', adult)
print(f'Ao todo temos {homem} homem(ns) cadastrado(s)')
print(f'E temos {mulher} mulher(es) com menos de 20 anos')
print('=-' * 21)