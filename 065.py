#065

opcao = ('s').upper()
soma = count = 0

while opcao == 'S':
  num = int(input('Digite um número: '))
  soma += num
  count += 1

  if count == 1:
    maior = menor = num
  else:
    if num > maior:
      maior = num
    if num < menor:
      menor = num
  
  opcao = input('Quer continuar? [S/N] ').upper().strip()[0]

else:
  print(f'Você digitou {count} números e a média é {soma / count}\nO maior valor foi de {maior} e o menor foi {menor}')
