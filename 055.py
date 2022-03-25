#055

maior = 0 
menor = 0

for x in range(1, 6):
  peso = int(input(f'Informe o peso da {x}ª pessoa: '))
  if x == 1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menos = peso

print(f'O maior peso foi {maior}Kg e o menor foi {menor}Kg.')