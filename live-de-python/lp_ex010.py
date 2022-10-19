# Faça um programa que leia 5 números e informe o maior número.

numero = 0
contador = 0
maior = 0

while contador != 5:
    contador += 1
    numero = float(input('Insira um número: '))
    if numero > maior:
        maior = numero
print(f'O maior número foi: {maior}')