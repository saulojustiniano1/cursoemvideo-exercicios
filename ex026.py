frase = str(input('Digite uma frase: ')).strip()

quantidade_de_letra_a = frase.upper().count('A')
posicao_da_primeira_letra_a = frase.upper().find('A') + 1
posicao_da_ultima_letra_a = frase.upper().rfind('A') + 1

print(f'A letra A aparece {quantidade_de_letra_a} vezes na frase')
print(f'A primeira letra A apareceu na posição {posicao_da_primeira_letra_a}')
print(f'A última letra A apareceu na posição {posicao_da_ultima_letra_a}')
