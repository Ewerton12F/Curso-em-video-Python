#051

print(f'''{'=' * 20}\n10 TERMOS DE UMA PA
{'=' * 20}''')

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 * razao)

for x in range(primeiro, decimo, razao):
  print(x, end=' ')
print('Acabô!')