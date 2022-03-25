#009

n = int(input('Digite um número para ver na tabuada: '))
print('-'*11)
print(f'{n} x {1:2.0f} = {n*1:2.0f}\n{n} x {2:2.0f} = {n*2:2.0f}\n{n} x {3:2.0f} = {n*3:2.0f}\n{n} x {4:2.0f} = {n*4:2.0f}\n{n} x {5:2.0f} = {n*5:2.0f}\n{n} x {6:2.0f} = {n*6:2.0f}\n{n} x {7:2.0f} = {n*7:2.0f}\n{n} x {8:2.0f} = {n*8:2.0f}\n{n} x {9:2.0f} = {n*9:2.0f}\n{n} x {10:2.0f} = {n*10}')
print('-'*11)

#009X

n = int(input())

for i in range(1,11):
  print(f'{i} x {n} = {i*n}')