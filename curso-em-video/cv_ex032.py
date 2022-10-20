# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year
    # Essa estrutura pega o ano atual.

# O ano bissexto é divisivel por quatro com exceção dos números divisiveis por 100 que não são divisiveis por 400.
if ano % 4 == 0 and (ano % 400 == 0 or ano % 100 != 0): 
    print(f'O ano {ano} é BISSEXTO')
else:
    print(f'O ano {ano} NÃO é BISSEXTO')
