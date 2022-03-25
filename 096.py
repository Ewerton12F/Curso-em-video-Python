#096

print('-' * 20)
print(f"{'Área':^20}")
print('-' * 20)

def area(l, c):
  a = l * c # return l * c
  print(f'A área de um terreno {l}x{c} é de {a}m².') # {area(l, c)}
  
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)