from random import randint

computador = randint(0, 10)
contador = 1

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
''')

jogador = int(input('Qual é seu palpite? '))

while jogador != computador:
  contador += 1

  if computador > jogador:
    print('Mais... Tente mais uma vez')
  else:
    print('Menos... Tente mais uma vez')

  jogador = int(input('Qual é seu palpite? '))

print(f'Acertou com {contador} tentativas. Parabéns!')
