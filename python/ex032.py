from datetime import date

ano = int(input('Que ano você quer analisar? Coloque 0 para analisar o ano atual: '))  # noqa

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 400 == 0 or ano % 4 == 0 and ano % 100 != 0:
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO É BISSEXTO')
