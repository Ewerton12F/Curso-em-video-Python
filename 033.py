#033

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

menor = a

if b < a and b < c:
  menor = b
if c < a and c < b:
  menor = c

maior = a

if b > a and b > c:
  maior = b
if c > b and c > a:
  maior = c

print(f'O menor número é {menor}\nO maior número é {maior}')