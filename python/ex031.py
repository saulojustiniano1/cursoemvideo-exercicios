distancia_da_viagem = float(input('Qual é a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia_da_viagem}Km.')

if distancia_da_viagem <= 200:
    valor_da_viagem = distancia_da_viagem * 0.50
    print(f'E o preço da sua passagem será de R${valor_da_viagem:.2f}')
else:
    valor_da_viagem = distancia_da_viagem * 0.45
    print(f'E o preço da sua passagem será de R${valor_da_viagem:.2f}')
