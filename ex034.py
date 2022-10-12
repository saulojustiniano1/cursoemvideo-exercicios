salario = float(input('Qual é o salário do funcionário? R$'))

if salario <= 1250:
  salario_novo = (salario * 0.15) + salario
else:
  salario_novo = (salario * 0.10) + salario

print(f'Quem ganhava R${salario:.2f} passa a ganhar R${salario_novo:.2f} agora.')
