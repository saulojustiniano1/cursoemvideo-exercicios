# Ainda fazendo!!!

numero = int(input('Digite um número: '))
opcao = str(input('Quer continuar: [S/N]: ')).upper()

maior = 0
menor = 0
media = 0
quant_numeros = 0

while opcao != 'N':
    maior = numero

    if numero > maior:
        maior = numero
    else:
        menor = numero

    quant_numeros += 1

    numero = int(input('Digite um número: '))
    opcao = str(input('Quer continuar: [S/N]: ')).upper()

print(f'Você digitou {quant_numeros} e a média foi de {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
