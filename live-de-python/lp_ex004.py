# Faça um programa que peça 2 números inteiros e 1 float. Calcule e mostre:
# - O produto do dobro do primeiro com metade do segundo
# - A soma do triplo do primeiro com o terceiro
# - O terceiro elevado ao cubo

numero_1 = int(input('Digite um número inteiro: '))
numero_2 = int(input('Digite outro número inteiro: '))
numero_3 = float(input('Digite um número decimal: '))

resultado_1 = (numero_1 * 2) * (numero_2 / 2)
resultado_2 = (numero_1 * 3) + numero_3
resultado_3 = numero_3 ** 3

print(f"""
    O produto do dobro do primeiro com metade do segundo é: {resultado_1}.
    A soma do triplo do primeiro com o terceiro é: {resultado_2}.
    O terceiro número elevado ao cubo é: {resultado_3}.
""")