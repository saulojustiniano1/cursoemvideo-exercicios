valores = []
contador = 0

while True:
    valor = int(input('Digite um valor: '))
    valores.append(valor)
    opcao = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    contador += 1

    if opcao == 'N':
        break

print('=-' * 20)
print(f'Você digitou {contador} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')

if 5 in valores:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não foi encontrado na lista.')
