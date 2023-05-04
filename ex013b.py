preco = float(input('Qual o preço do produto? R$'))

preco_aumento = preco * 0.08
preco_desconto = preco * 0.10

preco_a_vista = preco - preco_desconto
preco_parcelado = preco + preco_aumento

print(f'Caso você pague á vista o valor de R${preco:.2f} vai receber 15% de desconto, valor com desconto vai ficar de R${preco_a_vista:.2f}.')
print(f'Se você parcelar o valor de R${preco:.2f} vai acresentar 8% do preço atual, preço com aumento vai ficar de R${preco_parcelado:.2f}.')
