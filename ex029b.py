velocidade_do_carro = float(input('Qual é a velocidade atual do carro? '))

if velocidade_do_carro > 80:
  multa = (velocidade_do_carro - 80) * 7
  print('\033[31mMULTADO! Você excedeu o limite permitido que é de R$80Km/h\033[m')
  print(f'\033[31mVocê deve pagar uma multa de\033[m \033[32mR${multa:.2f}!\033[m')

print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
