valores = []
maior = -9999
menor = 9999

for i in range(5):
    valores.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-' * 20)

for valor in valores:
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ')
print(f'O menor valor digitado foi {menor}')
