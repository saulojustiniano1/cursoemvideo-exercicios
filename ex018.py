from math import sin, cos, tan, pi

angulo = float(input('Digite o ângulo que você deseja: '))

radiano = (angulo * pi) / 180

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f'O Ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O Ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O Ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
