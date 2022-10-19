# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cossento e tangente desse ângulo.

from math import radians, sin, cos, tan

angulo = float(input('Digite o ângulo que você deseja: '))
# O cálculo precisa da conversão para radianos para que o valor seja correto.
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')
