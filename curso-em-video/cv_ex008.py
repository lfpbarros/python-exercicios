# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metros = float(input('Uma distância em metros: '))
print(f'A medida de {metros:.1f}m corresponde a')
print(f'{metros / 1000}km') # Quilômetro
print(f'{metros / 100}hm') # Hectometro
print(f'{metros / 10}dam') # Decâmetro
print(f'{metros * 10:.0f}dm') # Decímetro
print(f'{metros * 100:.0f}cm') # Centímetro
print(f'{metros * 1000:.0f}mm') # Milímetro