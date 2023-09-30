from random import randint
from time import sleep

contador = 0

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 15)

while True:
    valor = int(input('Diga um valor: '))
    escolher = str(input('Par ou Ímpar? [P/I] ')).upper().strip()[0]

    computador = randint(1, 10)
    soma_geral = valor + computador

    if soma_geral % 2 == 0:
        print('-' * 20)
        print(
            f'Você jogou {valor} e o computador {computador}. Total de {soma_geral} DEU PAR')
        print('-' * 20)

        if escolher == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
            sleep(0.5)
            contador += 1
            continue
        else:
            print('Você PERDEU!')
            print('=-' * 15)

            print(f'GAME OVER! Você venceu {contador} vezes.')
            break

    elif soma_geral % 2 != 0:
        print('-' * 20)
        print(
            f'Você jogou {valor} e o computador {computador}. Total de {soma_geral} DEU ÍMPAR')
        print('-' * 20)

        if escolher == 'I':
            contador += 1
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('=-' * 15)
            sleep(0.5)
            continue

        else:
            print('Você PERDEU!')
            print('=-' * 15)
            print(f'GAME OVER! Você venceu {contador} vezes.')
            break
