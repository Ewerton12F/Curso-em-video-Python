#061

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
result = primeiro
count = 1

while count <= 10:
  print(result, ' → ' if count < 10 else ' → PAUSA', end=' ')
  result += razao
  count += 1