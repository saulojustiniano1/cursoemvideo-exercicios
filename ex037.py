numero = int(input('Digite um número inteiro: '))

print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

opcao = int(input('Sua opção: '))

if opcao == 1:
  binario = bin(numero)[2:]
  print(f'{numero} convertido para BINÁRIO é igual a {binario}')
elif opcao == 2:
  octal = oct(numero)[2:]
  print(f'{numero} convertido para OCTAL é igual a {octal}')
elif opcao == 3:
  hexadecimal = hex(numero)[2:]
  print(f'{numero} convertido para HEXADECIMAL é igual a {hexadecimal}')
else:
  print('Opção inválida. Tente novamente.')
