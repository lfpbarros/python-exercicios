# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Insira o peso da {i}ª pessoa: '))
    if peso > maior:
        maior = peso
    if i == 1:
        menor = peso
    else:
        if peso < menor:
            menor = peso

print(f'O maior peso lido foi de {maior:.1f}kg.')
print(f'O menor peso lido foi de {menor:.1f}kg.')
