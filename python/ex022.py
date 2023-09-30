nome = str(input('Digite seu nome completo: ')).strip()

maiusculo = nome.upper()
minuscula = nome.lower()
total_de_letras = len(nome) - nome.count(' ')  # Não sabia fazer esse!!!
primeiro_nome = nome.split()[0]
quantidade_de_letras_do_primeiro_nome = len(nome.split()[0])

print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {maiusculo}')
print(f'Seu nome em minúsculas é {minuscula}')
print(f'Seu nome tem ao todo {total_de_letras} letras')
print(
    f'Seu primeiro nome é {primeiro_nome} e ele tem {quantidade_de_letras_do_primeiro_nome} letras')  # noqa
