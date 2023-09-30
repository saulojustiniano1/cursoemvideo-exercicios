contador = 1

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))

    print('-' * 30)
    if valor < 0:
        break

    for contador in range(1, 11):
        print(f'{valor} x {contador} = {valor * contador}')
        contador += 1
    print('-' * 30)

print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
