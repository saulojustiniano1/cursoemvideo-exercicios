# Tenho que revisar esse exercício depois!!!

soma_da_idade = 0
media_de_idade = 0
maior_idade_do_homem = 0
nome_do_homem_mais_velho = ''
total_de_mulheres_com_menos_de_20_anos = 0

for p in range(1, 5):
  print(f'---- {p}ª PESSOA ----')
  nome = str(input('Nome: ')).strip()
  idade = int(input('Idade: '))
  sexo = str(input('Sexo [M/F]: ')).strip()
  
  soma_da_idade = soma_da_idade + idade

  if p == 1 and sexo in 'Mm':
    maior_idade_do_homem = idade
    nome_do_homem_mais_velho = nome
  if sexo in 'Mm' and idade > maior_idade_do_homem:
    maior_idade_do_homem = idade
    nome_do_homem_mais_velho = nome
  if sexo in 'Ff' and idade < 20:
    total_de_mulheres_com_menos_de_20_anos = total_de_mulheres_com_menos_de_20_anos + 1

media_da_idade = soma_da_idade / 4

print(f'A média de idade do grupo é de {media_da_idade} anos')
print(f'O homem mais velho tem {maior_idade_do_homem} anos e se chama {nome_do_homem_mais_velho}')
print(f'Ao todo {total_de_mulheres_com_menos_de_20_anos} mulhores com menos de 20 anos')
