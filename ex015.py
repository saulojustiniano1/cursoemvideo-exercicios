quantidade_de_dias = int(input('Quantos dias alugados? '))
quantidade_de_km = float(input('Quantos KM rodados? '))

valor_dias = quantidade_de_dias * 60
valor_km = quantidade_de_km * 0.15

preco_a_pagar = valor_dias + valor_km

print(f'O total a pagar é de R${preco_a_pagar:.2f}')
