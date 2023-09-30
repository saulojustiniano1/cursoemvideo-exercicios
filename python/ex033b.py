valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))
valor_3 = int(input('Terceiro valor: '))

# Verificando quem é o menor
menor = valor_1
if valor_2 < valor_1 and valor_2 < valor_3:
    menor = valor_2
if valor_3 < valor_1 and valor_3 < valor_2:
    menor = valor_3

# Vericando quem é o maior
maior = valor_1
if valor_2 > valor_1 and valor_2 > valor_3:
    maior = valor_2
if valor_3 > valor_1 and valor_3 > valor_2:
    maior = valor_3

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')
