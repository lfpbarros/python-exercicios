# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' LOJAS JOÃO SEM BRAÇO ')) # Uso da função format, o ^ centraliza a str na quantidade de espaços determinados, o = está ali para substituir os espaços
preco = float(input('Preço das compras: R$'))

print('''
FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    desconto = preco * 10/100
    preco_final = preco - desconto
elif opcao == 2:
    desconto = preco * 5/100
    preco_final = preco - desconto
elif opcao == 3:
    preco_final = preco
    valor_parcela = preco_final / 2
    print(f'Sua compra será parcelada em 2x de R${valor_parcela:.2f}')
elif opcao == 4:
    juros = preco * 20/100
    preco_final = preco + juros
    parcela = int(input('Quantas parcelas? '))
    valor_parcela = preco_final / parcela
    print(f'Sua compra será parcelada em {parcela}x de R${valor_parcela:.2f} COM JUROS')
else:
    print('Opção inválida! Tente novamente!')
print(f'Sua compra de R${preco:.2f} vai custar R${preco_final:.2f} no final')
