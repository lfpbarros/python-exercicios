# Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.

preco = float(input('Qual é o preço do produto? R$'))
desconto = preco * 0.05 # Ou preço * 5/100
novo_preco = preco - desconto
print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custar R${novo_preco:.2f}')
