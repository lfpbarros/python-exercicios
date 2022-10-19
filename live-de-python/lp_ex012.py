# Faça um programa que receba uma string com um numero de ponto flutuante e imprima qual a parte dele não é inteira.
# Ex: 
# n = '3.14'
# resposta = 14
# encontrei o find usando no terminal dir('')

numero = str(input('Insira um número de ponto flutuante: '))
posicao_ponto = numero.find('.')
casa_decimal = ''

for posicao, casa in enumerate(numero):
    if posicao > posicao_ponto:
        # print(casa)
        casa_decimal += casa
print(f'A casa decimal desse número é: {casa_decimal}')