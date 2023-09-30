valores = []

while True:
    valor = int(input('Digite um valor: '))

    if valor not in valores:
        valores.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        if valor in valores:
            print('Valor duplicado! Não vou adicionar...')

    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if opcao == 'N':
        break

print('=-' * 20)
valores.sort()
print(f'Você digitou os valores {valores}')
