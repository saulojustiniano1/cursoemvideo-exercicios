from random import choice

aluno_1 = str(input('Primeiro aluno(a): '))
aluno_2 = str(input('Segundo aluno(a): '))
aluno_3 = str(input('Terceiro aluno(a): '))
aluno_4 = str(input('Quarto aluno(a): '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]
escolhido = choice(lista)

print(f'A aluno(a) escolhido foi {escolhido}')
