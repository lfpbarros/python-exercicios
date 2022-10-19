# Faça um programa que pergunte o preço de três produtos, e informe qual é para comprar, o programa sempre escolhe o mais barato.

preço_1 = float(input('Preço 1: '))
preço_2 = float(input('Preço 2: '))
preço_3 = float(input('Preço 3: '))

if (preço_1 < preço_2) and (preço_1 < preço_3):
    print('Você deve comprar o primeiro')
elif (preço_2 < preço_1) and (preço_2 < preço_3):
    print('Você deve comprar o segundo')
elif (preço_3 < preço_1) and (preço_3 < preço_2):
    print('Você deve comprar o terceiro')
