# Faça um programa que receba uma data de nascimento (15/07/87) e imprima você nasceu <dia> de <mes> de <ano>.

# resposta = str(input('Qual é a sua data de nascimento? [xx/xx/xxxx] ')).split('/')

# print(f'Você nasceu em {resposta[0]} de {resposta[1]} de {resposta[2]}. ')

resposta = input('Qual é a sua data de nascimento? ')

dia, mes, ano = resposta.split('/')

print(f'Você nasceu em {dia} de {mes} de {ano}.')

