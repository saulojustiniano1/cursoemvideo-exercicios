print('=' * 30)
print('10 TERMOS DE UMA PA')
print('=' * 30)

primeira_termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

decimo_termo = primeira_termo + (10 - 1) * razao

for c in range(primeira_termo, decimo_termo + razao, razao):
    print(f'{c}', end=' → ')

print('ACABOU')
