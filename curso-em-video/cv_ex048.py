# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0

for i in range(1, 501):
# Podemos economizar os laços pulando de 2 em 2 já que queremos apenas os ímpares range(1, 501, 2)
    if i % 2 == 1 and i % 3 == 0:
        soma += i
        contador += 1

print(f'A soma de todos os {contador} valores solicitados é {soma}')
