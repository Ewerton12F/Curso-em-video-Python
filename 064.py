#064

num = count = soma = 0

num = int(input('Digite um número [999 para parar]: '))

while num != 999:
  soma += num
  count += 1
  num = int(input('Digite um número [999 para parar]: '))
print(f'Foram digitado {count} e a soma é {soma}')