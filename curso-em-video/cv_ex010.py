# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.
# Considere US$1.00 = R$3.27

reais = float(input('Quanto dinheiro você tem na carteira? R$'))
preco_dolar = 3.27
conversao = reais / preco_dolar
print(f'Com R${reais:.2f}, você pode comprar US${conversao:.2f}')
