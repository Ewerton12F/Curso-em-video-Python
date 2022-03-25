#042

a = int(input('Informe o tamanho do segmento a: '))
b = int(input('Informe o tamanho do segmento b: '))
c = int(input('Informe o tamanho do segmento c: '))


if abs(b - c) < a < b + c and abs(a - c) < b < a + c and abs(a - b) < c < a + b:
  print('Forma um triângulo', end= ' ')
  if a == b == c:
    print(f'equilátero.')
  elif a != b != c != a:
    print(f'escaleno.')
  elif a != b and b == c or b != c and a == c or c != a and b == a:
    print(f'isóceles.')
else:
  print('Os segmentos não formam um triângulo')