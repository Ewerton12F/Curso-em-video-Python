#073


L = ('um', 'dois', 'tres', 'quatro', 'cinco',
     'mquatro', 'mtres', 'mdois', 'mum')


print(L[:5])
print(L[-1:-5:-1])

for x in range(0, len(L)):
  print(x, end = ' ')
print('')
print(L.index('mquatro') + 1)
print(sorted(L)) 
print('~' * 13)