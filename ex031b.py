distancia_da_viagem = float(input('Qual a distância da sua viagem? '))

print(f'Você está prestes a começar uma viagem de {distancia_da_viagem}Km.')

valor_da_viagem = distancia_da_viagem * 0.50 if distancia_da_viagem <= 200 else distancia_da_viagem * 0.45

print(f'E p preço da sua passagem será de R${valor_da_viagem:.2f}')
