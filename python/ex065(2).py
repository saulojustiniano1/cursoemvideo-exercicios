responda = 'S'
media = soma = quant_valores = maior = menor = 0

while responda in 'Ss':
    numero = int(input('Digite um número: '))
    soma += numero
    quant_valores += 1

    if quant_valores == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    responda = str(input('Quer continuar? [S/N] ')).upper().strip()[0]

media = soma / quant_valores
print(f'Você digitou {quant_valores} números e a média foi de {media:.2f}')
print(f'O maior valor foi de {maior} e o menor foi de {menor}')
