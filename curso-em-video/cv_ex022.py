# Crie um programa que leia o nome completo de uma pessoa e mostre:
#   -> O nome com todas as letras maiúsculas e minúsculas.
#   -> Quantas letras ao todo (sem considerar espaços).
#   -> Quantas letras tem o primeiro nome.

from time import sleep

nome = str(input('Digite seu nome completo: ')).strip() # Elimina os espaços antes e depois 
nome_separado = nome.split() # Separando os nomes por espaço
qtd_letras = len(nome) - nome.count(' ')
print('Analisando o seu nome... ')
sleep(2) # Apenas para dar aquela impressão de análise.
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome ao todo tem {qtd_letras} letras')
print(f'Seu primeiro nome é {nome_separado[0]} e ele tem {len(nome_separado[0])} letras')
