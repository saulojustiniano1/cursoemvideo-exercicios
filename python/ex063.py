print('-' * 25)
print('Sequência de Fibonacci')
print('-' * 25)

quantos_termos = int(input('Quantos termos você quer mostrar? '))

termo_1 = 0
termo_2 = 1

print('~' * 25)
print(f'{termo_1} -> {termo_2}', end='')

contador = 3

while contador <= quantos_termos:
    termo_3 = termo_1 + termo_2
    print(f' -> {termo_3}', end='')

    termo_1 = termo_2
    termo_2 = termo_3
    contador += 1

print(' -> FIM!')
print('~' * 25)
