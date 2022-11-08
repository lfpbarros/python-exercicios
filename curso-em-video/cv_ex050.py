# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for i in range(6):
    n = int(input(f'Digite o {i + 1}º valor: '))
    if n % 2 == 0:
        soma += n
        contador += 1

print(f'Você informou {contador} números pares e soma deles é de {soma}')
