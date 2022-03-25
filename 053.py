#053

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1 , -1):
  inverso += junto[letra]
print(junto, inverso)
if frase == inverso:
  print('Palíndromo!')
else:
  print('Não é palíndromo!')

# Sem for

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]

print(junto, inverso)
if frase == inverso:
  print('Palíndromo!')
else:
  print('Não é palíndromo!')