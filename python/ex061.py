# Não consegui fazer esse exercicios. Tenho que APRENDER!!!

print('Gerador de PA')
print('-=' * 10)

primeiro_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

termo = primeiro_termo
contador = 1

while contador <= 10:
    print(f'{termo} -> ', end='')
    termo = termo + razao
    contador = contador + 1

print('FIM')
