#022

nome = input('Dígite seu nome: ').strip()

print('Analisando o seu nome...')
print(f'Seu nome em maiúsculo é {nome.upper()}')
print(f'Seu nome em minúscolo é {nome.lower()}')

letras = len(nome) - nome.count(' ')

print(f'Seu nome tem ao todo {letras} letras')

dividido = nome.split()

print(f'Seu primeiro nome é {dividido[0]} e ele tem {len(dividido[0])} letras')