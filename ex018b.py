from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))

radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'O Ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O Ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O Ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
