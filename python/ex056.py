# Tenho que revisar esse exercício depois!!!

soma_idade = 0
media_idade = 0
maior_idade_homem = 0
total_mulheres_menos_20_anos = 0
homem_mais_velho = ''

for i in range(1, 2):
    print(f'---- {i}ª PESSOA ----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()

    soma_idade = soma_idade + idade

    if i == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        homem_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulheres_menos_20_anos = total_mulheres_menos_20_anos + 1

media_idade = soma_idade / 4

print(f'A média de idade do grupo é de {media_idade} anos')
print(
    f'O homem mais velho tem {maior_idade_homem} anos'
    f'e se chama {homem_mais_velho}')
print(
    f'Ao todo {total_mulheres_menos_20_anos} mulhores com menos de 20 anos')
