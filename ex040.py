nota_1 = float(input('Primeira nota: '))
nota_2 = float(input('Segundo nota: '))

media = (nota_1 + nota_2) / 2

print(f'Tirando {nota_1:.1f} e {nota_2:.1f}, a média do aluno é {media:.1f}')

if media >= 7:
    print('O aluno está APROVADO!')
elif media >= 5 and media < 7:
    print('O aluno está em RECUPERAÇÃO!')
elif media < 5:
    print('O aluno está REPROVADO!')
