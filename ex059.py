from time import sleep

fechar = False

valor_1 = int(input('Primeiro valor: '))
valor_2 = int(input('Segundo valor: '))

while not fechar:
  print('''  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa''')
  opcao = int(input('>>>>> Qual é sua opção? '))

  if opcao == 1:
    soma = valor_1 + valor_2
    print(f'A soma entre {valor_1} + {valor_2} é {soma}')
  elif opcao == 2:
    multiplicar = valor_1 * valor_2
    print(f'O resultado de {valor_1} x {valor_2} é {multiplicar}')
  elif opcao == 3:
    if valor_1 > valor_2:
      print(f'Entre {valor_1} e {valor_2} o maior valor é {valor_1}')
    else:
      print(f'Entre {valor_1} e {valor_2} o maior valor é {valor_2}')
  elif opcao == 4:
    print('Informe os números novamento: ')
    valor_1 = int(input('Primeiro valor: '))
    valor_2 = int(input('Segundo valor: '))
  elif opcao == 5:
    print('Finalizando...')
    fechar = True
  else:
    print('Opção inválida. Tente novamento')
  print('=-=' * 10)
  sleep(1)
  
print('Fim do programa! Volte sempre')
