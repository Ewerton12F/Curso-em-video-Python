#72
count = ('zero', 'um', 'dois', 'três', 'quatro',
         'cinco', 'seis', 'sete', 'oito', 'nove',
         'dez', 'onze', 'doze', 'treze', 'catorze',
         'quize', 'dezesseis', 'dezessete', 'dezoito',
         'desenove', 'vinte')

resposta = 0

while True:
  num = int(input('Entre 0 e 20 '))
  if 0 <= num <= 20:
    break
  print('Tente novamente.', end = ' ')
print(f'Você digitou o número {count[num]}')
