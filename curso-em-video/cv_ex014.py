# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input('Informe a temperatura em ºC: '))
f = c * 1.8 + 32 # ((9 * C) / 5) + 32 - fórmula para conversão.
print(f'A temperatura de {c}ºC corresponde a {f:.1f}ºF! ')