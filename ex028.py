from random import randint
from time import sleep

computador = randint(0, 5) # Faz o computador "PENSAR"

print('\033[33m-=-\033[m' * 20)
print('\033[36mVou pensar em um número entre 0 e 5. tente adivinhar...\033[m')
print('\033[33m-=-\033[m' * 20)

jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar

print('\033[33mPROCESSANDO...\033[m')
sleep(2)

if jogador == computador:
  print('\033[32mPARABÉNS! Você conseguiu me vencer!\033[m')
else:
  print(f'\033[31mGANHEI! Eu pensei no número {computador} e não no {jogador}!\033[m')
