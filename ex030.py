numero = int(input('\033[35mMe diga um número qualquer: \033[m'))

if numero % 2 == 0:
  print(f'O número {numero} é \033[32mPAR\033[m')
else:
  print(f'O número {numero} é \033[31mÍMPAR\033[m')
