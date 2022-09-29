salario_do_funcionario = float(input('Qual é o salário do funcionário? R$'))

salario_aumento = salario_do_funcionario * 0.15
salario_final = salario_do_funcionario + salario_aumento

print(f'Um funcionário que ganhava R${salario_do_funcionario:.2f}, com 15% de aumento, passa a receber R${salario_final:.2f}')
