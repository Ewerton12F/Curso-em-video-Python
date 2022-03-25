#038

primeiro = int(input('Primeiro número: '))
segundo = int(input('Segundo número: '))

if primeiro > segundo:
  print(f'O número {primeiro} é o maior!')
if segundo > primeiro:
  print(f'O número {segundo} é o maior!')
if primeiro == segundo:
  print('Os dois valores são iguais!')