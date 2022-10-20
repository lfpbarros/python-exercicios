# Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra "A".
# -> Em que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a última vez.

frase = str(input('Digite uma frase: ')).strip().lower()
contagem = frase.count('a')
posicao_inicio = frase.find('a') + 1 # O + 1 ajuda a corrigir já que os índices do Python começam no 0
posicao_final = frase.rfind('a') + 1
print(f'A letra A aparece {contagem} vezes na frase.')
print(f'A primeira letra A apareceu na posição {posicao_inicio}')
print(f'A última letra A apareceu na posição {posicao_final}')
