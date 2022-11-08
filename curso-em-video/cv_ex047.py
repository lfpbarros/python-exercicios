# Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

for i in range(1, 51):
# Podemos diminuir o número de iterações por ir pulando de 2 em 2 range(2, 51, 2)
    if i % 2 == 0:
        print(i, end=', ')
print('Acabou')

