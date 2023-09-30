pessoas = []
dados = []
quant_pessoas = maior_peso = menor_peso = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    quant_pessoas += 1
    opcao = ' '

    while opcao not in 'SN':
        opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if opcao == 'N':
        break

for p in pessoas:
    if len(pessoas) == 0:
        maior_peso = menor_peso = p[1]
    else:
        if p[1] > maior_peso:
            maior_peso = p[1]
        if p[1] < menor_peso:
            menor_peso = p[1]

print('=-' * 20)
print(f'Ao todo, você cadastrou {quant_pessoas} pessoas.')
print(f'O maior peso foi de {maior_peso}Kg.')
print(f'O menor peso foi de {menor_peso}Kg.')
