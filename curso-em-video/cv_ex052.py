# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

num = int(input('Insira um número: '))
contador = 0

for i in range(num - 1, 1, -1):
    if num % i == 0:
        contador += 1

if num == 1 or num == 0 or num < 0:
    contador += 1

if contador == 0:
    print(f'O número {num} é primo')
else:
    print(f'O número {num} não é primo')