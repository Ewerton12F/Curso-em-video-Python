#077

palavra = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS',
           'ESTUDAR', 'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

a = e = i = o = u = 0

for x in palavra:
  print(f'\nNa palavra {x} temos', end = ' ')
  for letra in x:
    if letra.lower() in 'aeiou':
      print(letra, end = ' ')