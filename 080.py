#080

Lnum = []

for x in range(0, 5):
  num = int(input('Digite um valor: '))

  if x == 0 or num > Lnum[-1]:
    Lnum.append(num)
    print('Adicionado ao final da lista...')
  
  else:
    pos = 0
    while pos < len(Lnum):
      if num <= Lnum[pos]:
        Lnum.insert(pos, num)
        print(f'Adicionando na posição {pos + 1} da linha...')
        break
      pos += 1  

print('-' * 30)
print('Os valores digitados em ordem são:', Lnum)