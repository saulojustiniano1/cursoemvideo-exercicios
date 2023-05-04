from random import shuffle

aluno_1 = str(input('Primero aluno(a): '))
aluno_2 = str(input('Segundo aluno(a): '))
aluno_3 = str(input('Terceiro aluno(a): '))
aluno_4 = str(input('Quarto aluno(a): '))

lista = [aluno_1, aluno_2, aluno_3, aluno_4]

shuffle(lista)

print('A ordem de apresentação será:')
print(lista)
