#043

kg = float(input('Informe o peso: '))
m = float(input('Informe a altura: '))

imc = kg / (m ** 2)

print(f'O IMC é de {imc:.1f}.')

if 18.5 > imc:
  print('Abaixo do peso!')
elif 18.5 < imc <= 25:
  print('Peso ideal!') 
elif 25 < imc <= 30:
  print('Sobrepeso!')
elif 30 < imc <= 40:
  print('Obesidade!')
else:
  print('Obesidade mórbida!')