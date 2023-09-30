largura = float(input('Largura da parede: '))
altura = float(input('Altura da parede: '))

area = largura * altura
litro_de_tinta = area / 2

print(
    f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².')  # noqa
print(
    f'Para pintar essa parede, você precisará de {litro_de_tinta}L de tinta.')
