# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostra a sua média.

nota_1 = float(input('Primeira nota do aluno: '))
nota_2 = float(input('Segunda nota do aluno: '))
media = (nota_1 + nota_2) / 2
print(f'A média entre {nota_1} e {nota_2} é igual a {media:.1f}.')
