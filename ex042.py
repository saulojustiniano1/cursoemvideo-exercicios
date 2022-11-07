a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if (b - c) < a < b + c and (a - c) < b < a + c and (a - b) < c < a + b:
  if a == b == c:
    print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO')
  elif a != b != c != a:
    print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO')
  else:
    print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES')
else:
  print('Os segmentos acima NÃO PODEM FORMAR triângulo')
