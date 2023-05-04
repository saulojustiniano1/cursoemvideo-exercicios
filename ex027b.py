nome = str(input('Digite seu nome completo: ')).strip()

lista_nome = nome.split()
primeiro_nome = lista_nome[0]
ultimo_nome = lista_nome[len(lista_nome)-1]

print('Muito prazer te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
