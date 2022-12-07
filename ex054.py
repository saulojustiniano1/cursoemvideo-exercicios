from datetime import date

ano_atual = date.today().year

maiores = 0
menores = 0

for c in range(1, 8):
  ano_de_nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
  
  idade = ano_atual - ano_de_nascimento

  if idade >= 21:
    maiores = maiores + 1
  else:
    menores =  menores + 1

print(f'Ao todo tivemos {maiores} pessoas maiores de idade')
print(f'E também tivemos {menores} pessoas menores de idade')
