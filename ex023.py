numero = int(input('Informe um número: '))

unidade = numero / 10
unidade_real = int(numero % 10)

dezena = unidade / 10
dezena_real = int(unidade % 10)

centena = dezena / 10
centena_real = int(dezena % 10)

milhar_real = int(centena)

print(f'Analisando o número {numero}')
print(f'Unidade: {unidade_real}')
print(f'Dezena: {dezena_real}')
print(f'Centena: {centena_real}')
print(f'Milhar: {milhar_real}')
