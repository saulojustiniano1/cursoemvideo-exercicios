from math import pow, sqrt

cateto_aposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

hipotenusa = sqrt((pow(cateto_aposto, 2)) + (pow(cateto_adjacente, 2)))

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
