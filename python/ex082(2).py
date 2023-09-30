valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

    if opcao == 'N':
        break

for i, c in enumerate(valores):
    if c % 2 == 0:
        pares.append(c)
    elif c % 2 != 0:
        impares.append(c)

print('=-' * 20)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
