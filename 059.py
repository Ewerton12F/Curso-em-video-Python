#059

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
a = '=-='

while True:
  print(f'{a * 10}\n| 1 | SOMAR\n| 2 | MULTIPLICAR\n| 3 | MAIOR\n| 4 | NOVOS NÚMEROS\n| 5 | SAIR DO PROGRAMA\n{a * 10}')
  escolha = int(input('Qual é a sua opção? '))
  if escolha == 1:
    print(f'A soma entre {primeiro} + {segundo} é {primeiro + segundo}')
  if escolha == 2:
    print(f'A multiplicação entre {primeiro} x {segundo} é {primeiro * segundo}')
  if escolha == 3:
    if primeiro > segundo:
      print(f'O número {primeiro} é maior que o {segundo}')
    else:
      print(f'O número {segundo} é maior que o {primeiro}')
  if escolha == 4:
    primeiro = int(input('Primeiro valor: '))
    segundo = int(input('Segundo valor: '))
  if escolha== 5:
    print('Saiu!')
    break