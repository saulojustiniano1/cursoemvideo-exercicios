from math import pow, sqrt

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))

b = pow(cateto_oposto, 2)
c = pow(cateto_adjacente, 2)

hipotenusa = sqrt((pow(cateto_oposto, 2)) + (pow(cateto_adjacente, 2)))

print('a² = b² + c²')
print(f'a² = {cateto_oposto}² + {cateto_adjacente}²')
print(f'a² = {b} + {c}')
print(f'a² = {b + c}')
print(f'a  = √{b + c}')
print(f'a  = {hipotenusa:.2f}')
