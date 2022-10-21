# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Valor da casa: R$'))
salario_comprador = float(input('Salário do comprador: R$'))
tempo_financiamento_anos = int(input('Quantos anos de financiamento? '))
tempo_financiamento_meses = tempo_financiamento_anos * 12
# Para já trazer o valor em meses do tempo do financiamento, já estou multiplicando por 12.
prestacao = valor_casa / tempo_financiamento_meses

print(f'Para pegar uma casa de R${valor_casa:.2f} em {tempo_financiamento_anos} anos, a prestação será de R${prestacao:.2f}')

if prestacao <= salario_comprador * 30/100:
    print('Empréstimo pode ser CONCEDIDO!')
elif prestacao > salario_comprador * 30/100:
    print('Empréstimo NEGADO!')
    
