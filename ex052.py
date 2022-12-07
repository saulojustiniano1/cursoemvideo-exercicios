# Tenho que revisar esse exercício depois!!!

numero = int(input('Digite um número: '))

total_de_primos = 0

for c in range(1, numero + 1):
  if numero % c == 0:
    print('\033[33m', end=' ')
    total_de_primos = total_de_primos + 1
  else:
    print('\033[31m', end=' ')
  
  print(f'{c}', end=' ')

print(f'\n\033[mO número {numero} foi divisivel {total_de_primos} vezes.')

if total_de_primos == 2:
  print('E por isso ele É PRIMO!')
else:
  print('E por isso ele NÃO É PRIMO!')
