# Não consegui fazer esse exercicios. Tenho que APRENDER!!!

numero = int(input('Digite um número para calcular seu factorial: '))

factorial = 1

print(f'Calculando {numero}! = ', end='')

for contador in range(numero, 0, -1):
  print(f'{contador}', end='')
  print(' x ' if contador > 1 else ' = ', end='')
  factorial = factorial * contador

print(f'{factorial}', end='')