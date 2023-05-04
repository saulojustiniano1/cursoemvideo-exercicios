# Não consegui fazer esse exercicios. Tenho que APRENDER!!!

print('Gerador de PA')
print('-=' * 10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro_termo
contador = 1
total_de_termos = 0
termos_mais = 10

while termos_mais != 0:
  total_de_termos = total_de_termos + termos_mais

  while contador <= total_de_termos:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    contador = contador + 1 

  print('PAUSA')

  termos_mais = int(input('Quantos termos você quer mostrar a mais? '))

  print(f'Progressão finalizada com {total_de_termos} termos mostrados.')
  
print('FIM')
