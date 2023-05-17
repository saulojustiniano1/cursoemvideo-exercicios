soma = 0
contador = 0

for c in range(1, 7):
    numero = int(input(f'Digite o {c}° valor: '))

    if numero % 2 == 0:
        contador = contador + 1
        soma = soma + numero

print(f'Você informou {contador} números PARES e a soma {soma}')
