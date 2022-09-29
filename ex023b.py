numero = str(input('Informe um número: '))

unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

# Só funciona quando tem os 4 digitos digitados
print(f'Analisando o número {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
