# Não consegui fazer esse exercicios. Tenho que APRENDER!!!

numero = int(input('Digite um número para\ncalcular seu Factorial: '))

contador = numero
factorial = 1

print(f'Calculando {numero}! = ',end='')

while contador > 0:
  print(f'{contador}', end='')
  print(' x ' if contador > 1 else ' = ', end='')
  factorial = factorial * contador
  contador = contador - 1

print(f'{factorial}')
