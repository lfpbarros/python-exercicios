# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos

media_idade = 0
homem_mais_velho = ''
idade_homem_mais_velho = 0
cont_mulheres_menos_de_20 = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input(f'Nome: ')).strip().capitalize()
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo: [M / F] ')).strip().upper()[0]
    media_idade += idade
    if sexo == "M" and idade > idade_homem_mais_velho:
        homem_mais_velho = nome
        idade_homem_mais_velho = idade
    if sexo == "F" and idade < 20:
        cont_mulheres_menos_de_20 += 1

media_idade = media_idade / i

print(f'A média de idade do grupo é de {media_idade:.1f}')
if homem_mais_velho != '':
    print(f'O nome do homem mais velho é {homem_mais_velho} e sua idade é {idade_homem_mais_velho} anos')
print(f'E {cont_mulheres_menos_de_20} mulheres tem idade menor que 20 anos.')
