contador = 1

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))

    if valor < 0:
        print('-' * 30)
        print('PROGRAMA TABUADA ENCERRADA. Volte sempre!')
        break

    print('-' * 30)
    while contador < 11:
        print(f'{valor} x {contador} = {valor * contador}')
        contador += 1
    print('-' * 30)

    if contador == 11:
        contador = 1
        continue
