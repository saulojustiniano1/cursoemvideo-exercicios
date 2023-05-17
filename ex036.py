valor_da_casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
quantos_anos_financiamento = int(input('Quantos anos de financiamento: '))

prestacao = valor_da_casa / (quantos_anos_financiamento * 12)
valor_minino = salario * 0.3

print(
    f'Para pagar uma casa de R${valor_da_casa:.2f} em {quantos_anos_financiamento} anos a prestação será de R${prestacao:.2f}')  # noqa

if prestacao <= valor_minino:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
