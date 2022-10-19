# Programa que pede o tamanho em metros quadrados de uma área. Para 3 metros, 1 litro de tinta. 1 lata tem 18 litros. 1 lata custa R$ 80,00.

from math import ceil

# Essa é um módulo para arredondar para cima já que mesmo que a pessoa comprar só um litro, ela precisa comprar a lata inteira.

print("*/\* Loja de tintas */\*\n")

metros = int(input('Quantos metros quadrados de área serão pintados? '))

litros = metros / 3
latas = ceil(litros / 18)
preco = latas * 80

print(f'Para essa área serão necessárias {latas} latas. O valor total da compra é de R${preco:.2f}')

# print(litros)
# print(latas)