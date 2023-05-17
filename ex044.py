print('{:=^40}'.format(' LOJAS GUANABARA '))

preco_das_compras = float(input('Preço das compras: R$'))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')

opcao = int(input('Qual sua opção? '))

if opcao == 1:
    valor = preco_das_compras - (preco_das_compras * 0.10)
elif opcao == 2:
    valor = preco_das_compras - (preco_das_compras * 0.05)
elif opcao == 3:
    valor = preco_das_compras
    parcela = valor / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opcao == 4:
    valor = preco_das_compras + (preco_das_compras * 0.20)
    parcelas = int(input('Quantas parcelas? '))
    parcela = valor / parcelas
    print(
        f'Sua compra será parcelada em {parcelas}x de R${parcela:.2f} COM JUROS')
else:
    valor = preco_das_compras
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print(
    f'Sua compra de R${preco_das_compras:.2f} vai custar R${valor:.2f} no final')
