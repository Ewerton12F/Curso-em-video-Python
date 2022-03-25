#044

print('=' * 12, 'MERCADO', '=' * 12)

preco = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO:
[ 1 ] à vista (dinheiro/cheque)
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))


if opcao == 1:
  print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco - (preco * (10 / 100)):.2f}')
elif opcao == 2:
  print(f'Sua compra de R$ {preco:.2f} vai custar R$ {preco - (preco * (5 / 100)):.2f}')
elif opcao == 3:
  print(f'Sua compra será parcelada em 2x de R${preco / 2:.2f}. Sua compra vai custar R$ {preco:.2f}')
elif opcao == 4:
  parcela = int(input('Quantas parcelas? '))
  print(f'Sua compra será parcelada em {parcela}x de R$ {(preco + (preco * (20 / 100))) / parcela:.2f}\nSua compra de R$ {preco:.2f} vai custar R$ {preco + (preco * (20 / 100)):.2f}')
else:
  print('Escolha uma opção válida!')