#036

casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salário: R$'))
anos = int(input('Anos a pagar: '))

prestacao = casa / (anos * 12)

print(f'Para pagar um casa de R${casa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')

if prestacao <= salario * 0.3:
  print('Emprestimo APROVADO!')
else:
  print('Emprestimo NEGADO!')