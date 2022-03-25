#031

distancia = int(input('Informe a distância: '))

if distancia <= 200:
  print(f'Você está prestes a começar uma viagem de {distancia}.\nE o preço da sua passagem será de R${distancia * 0.5:.2f}')
else:
  print(f'Você está prestes a começar uma viagem de {distancia}.\nE o preço da sua passagem será de R${distancia * 0.45:.2f}')

'''
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
print('O preço da sua passagem será de R${preco:.2f})'''