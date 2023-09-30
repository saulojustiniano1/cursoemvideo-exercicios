valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
valor_3 = int(input('Terceiro valor: '))

if valor_1 > valor_2 and valor_1 > valor_3:
    if valor_2 > valor_3:
        print(f'O menor valor digitado foi {valor_3}')
        print(f'O maior valor digitado foi {valor_1}')
    if valor_2 < valor_3:
        print(f'O menor valor digitado foi {valor_2}')
        print(f'O maior valor digitado foi {valor_1}')
if valor_2 > valor_1 and valor_2 > valor_3:
    if valor_1 > valor_3:
        print(f'O menor valor digitado foi {valor_3}')
        print(f'O maior valor digitado foi {valor_2}')
    if valor_1 < valor_3:
        print(f'O menor valor digitado foi {valor_1}')
        print(f'O maior valor digitado foi {valor_2}')
if valor_3 > valor_1 and valor_3 > valor_2:
    if valor_2 > valor_1:
        print(f'O menor valor digitado foi {valor_1}')
        print(f'O maior valor digitado foi {valor_3}')
    if valor_2 < valor_1:
        print(f'O menor valor digitado foi {valor_2}')
        print(f'O maior valor digitado foi {valor_3}')
