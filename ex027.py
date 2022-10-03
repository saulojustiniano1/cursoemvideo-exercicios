nome = str(input('Digite seu nome completo: ')).strip()

primeiro_nome = nome.split()[0]
ultimo_nome = nome.split()[-1]

print('Muito prazer em te conhecer!')
print(f'Seu primeiro nome é {primeiro_nome}')
print(f'Seu último nome é {ultimo_nome}')
