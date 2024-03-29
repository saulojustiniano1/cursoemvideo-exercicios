from datetime import date

ano_de_nascimento = int(input('Ano de nascimento: '))

ano_atual = date.today().year
idade = ano_atual - ano_de_nascimento

print(f'Quem nasceu em {ano_de_nascimento} tem {idade} anos em {ano_atual}')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    falta = 18 - idade
    print(f'Ainda faltam {falta} anos para o alistamento.')
    ano = ano_atual + falta
    print(f'Seu alistamento será em {ano}')
elif idade > 18:
    passou = idade - 18
    print(f'Você já deveria ter se alistado há {passou} anos.')
    ano = ano_atual - passou
    print(f'Seu alistamento foi em {ano}')
