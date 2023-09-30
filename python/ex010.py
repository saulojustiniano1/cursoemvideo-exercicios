real = float(input('Quanto dinheiro você tem na carteira? R$'))

dolar = real / 5.15
euro = real / 5.23

print('====== DÓLAR ======')
print(f'Com R${real:.2f} você pode comprar U${dolar:.2f}')

print('====== EURO ======')
print(f'Com R${real:.2f} você pode cpmprar €${euro:.2f}')
