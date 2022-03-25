#034

salario = float(input('Qual o salário do funcionário? '))

atual = salario + (salario * 0.15) if salario <= 1250 else salario + (salario * 0.1)

print(f'Quem grnhava R${salario:.2f} passa a ganhar R${atual:.2f}')