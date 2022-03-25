#050

par = 0

for x in range(1, 7):
  num = int(input('Digite um valor: '))
  if num % 2 == 0:
    par += num
print('A soma dos números pares é: ', par)