#019

import random

x = 1

for x in range(1, 5):
  nome = str(input(f'Informe o nome do {x}º aluno: '))
  if x == 1:
    nome1 = nome
    x1 = x
  if x == 2:
    nome2 = nome
    x2 = x
  if x == 3:
    nome3 = nome
    x3 = x    
  if x == 4:
    nome4 = nome
    x4 = x    
  x += 1
print(f'O {x1}º aluno é: {nome1}\nO {x2}º aluno é: {nome2}\nO {x3}º aluno é: {nome3}\nO {x4}º aluno é: {nome4}\n')

lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'O aluno escolhido foi {escolhido}')