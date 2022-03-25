#062

primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
result = primeiro
count = 1

while count <= 10:
  print(result, ' → ' if count < 10 else '→ PAUSA', end=' ')
  result += razao
  count += 1

while True:
  
  mais = int(input('\nQuantos termos você quer mostrar a mais? '))

  if mais > 0:
    for x in range(0, mais):
      print(result, ' → ' if x <= mais else 'PAUSA', end=' ') 
      result += razao
    count += mais
  else:
    print(f'Prograssão finalizada com {count - 1} termos mostrados.')
    break