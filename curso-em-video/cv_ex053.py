# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma palavra para saber se é palíndromo: ')).lower().strip()
contrario = ''
frase_sem_espaco = frase.split()
frase_sem_espaco = ''.join(frase_sem_espaco)

for i in range(len(frase) -1, -1, -1):
    if frase[i] != ' ':
        contrario += frase[i]

if frase_sem_espaco == contrario:
    print(f'{frase.capitalize()} é um palíndromo.')
else:
    print(f'{frase.capitalize()} não é um palíndromo.')
