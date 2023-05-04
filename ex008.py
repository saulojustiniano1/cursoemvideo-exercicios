medida = float(input('Uma distância em metros: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'A medida de {medida}m corresponde a: ')
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{dm:.0f}dm')
print(f'{cm:.0f}cm')
print(f'{mm:.0f}mm')
