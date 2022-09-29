preco = float(input('Qual é o preço do produto? R$'))

preco_com_desconto = preco * 0.05
preco_final = preco - preco_com_desconto

print(f'O produto que custava R${preco:.2f}, na promoção com desconto de 5% vai custar R${preco_final:.2f}')
