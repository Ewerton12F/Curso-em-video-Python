#058

from random import randint

computador = randint(0, 11)
tentativa = 0

adivinhar = int(input('Sou seu computador...\nAcabei de pensar em um número entre 0 e 10.\nSerá que você consegue adivinhar qual foi?\nQual é o seu palpite? '))

while computador != adivinhar:
  if adivinhar < computador:
    print('Mais... Tente mais uma vez.')
    adivinhar = int(input('Qual o seu palpite? '))
  else:
    print('Menos... Tente mais uma vez.')
    adivinhar = int(input('Qual o seu palpite? '))
  tentativa += 1
print(f'Acertou com {tentativa + 1} tentativa(s). Parabéns!')