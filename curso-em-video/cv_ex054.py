# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

maioridade = 0
menoridade = 0
ano_atual = date.today().year

for i in range(1, 8):
    ano_nascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    if ano_atual - ano_nascimento >= 21:
        maioridade += 1
    else:
        menoridade += 1

print(f'Ao todo, tivemos {maioridade} pessoas maiores de idade')
print(f'E também tivemos {menoridade} pessoas menores de idade')