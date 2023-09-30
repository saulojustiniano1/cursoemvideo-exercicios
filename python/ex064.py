numero = int(input('Digite um número [999 para parar]: '))
soma = 0
quant_numeros = 0

while numero != 999:
    soma += numero
    quant_numeros += 1

    numero = int(input('Digite um número [999 para parar]: '))

print(
    f'Você digitou {quant_numeros} números e a soma entre eles foi de {soma}')
