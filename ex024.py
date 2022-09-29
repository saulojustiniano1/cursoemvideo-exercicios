cidade = str(input('Em que cidade você nasceu? ')).strip()

santos_verificacao = cidade.upper().split()[0] == 'SANTO'

print(santos_verificacao)
