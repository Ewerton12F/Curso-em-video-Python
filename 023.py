#023

numero = input('Informe um número: ')

print(f'Analisando o número {numero}')

print(f'Unidade: {numero[-1]}')
print(f'Dezena: {numero[-2]}')
print(f'Centena: {numero[-3]}')
print(f'Milhar: {numero[-4]}')
print(f'Dezena de Milhar: {numero[-5]}')
print(f'Centena de Milhar: {numero[-6]}')
print(f'Milhão: {numero[-7]}')

#023

numero = input('Informe um número: ')

for x in range(0, len(numero)):
  if numero[x] != -1:
    print(f'Unidade: {numero[x]}')
    x -= 1