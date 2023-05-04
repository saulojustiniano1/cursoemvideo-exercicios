# Tenho que revisar esse exercício depois!!!

frase = str(input('Digite uma frase: ')).strip().upper()

palavras = frase.split()
juncao = ''.join(palavras)
inverso = ''

for letra in range(len(juncao) - 1, -1, -1):
  inverso = inverso + juncao[letra]

print(f'O inverso de {juncao} é {inverso}')

if inverso == juncao:
  print('Temos um palíndromo!')
else:
  print('A frase digitada não é um palíndromo!')
