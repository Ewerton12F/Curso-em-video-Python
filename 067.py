#067

while True:
  print('~' * 35)
  num = int(input('Quer ver a tabuada de qual valor? '))
  if num == 0:
    print('~' * 35)
    print('Parar')
    print('~' * 5)
    break
  print('~' * 35)
  for x in range(1, 11):
    print(f'{num} x {x:2.0f} = {num * x}')