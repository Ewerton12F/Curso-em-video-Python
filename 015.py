#015

dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos km rodados? '))

print(f'O valor a pagar será R${(dias * 60) + (km * 0.15):.2f}.')