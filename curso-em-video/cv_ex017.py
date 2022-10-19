# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

cateto_oposto = float(input('Comprimento do cateto oposto: '))
cateto_adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')

# Fórmula sem a função: (cateto_oposto ** 2 + cateto_adjacente ** 2) ** (1/2)

