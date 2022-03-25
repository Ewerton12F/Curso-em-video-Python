# 029

velocidade = int(input('Qual a velocidade atual do carro? '))

if velocidade <= 80:
  multa = 7 * (velocidade - 80)
  print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h.\nVocê deve pagar uma multa de R$ {multa:.2f}\nTenha um bom dia! Dirija com segurança!')
print('Tenha um bom dia! Dirija com segurança!')