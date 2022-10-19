# O mesmo professor do desafio anterior quer sortear a ordem de aprensentação de trabalhos dos alunos. Faça um programa que leia o nomes dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

aluno_1 = str(input('Primeiro aluno: '))
aluno_2 = str(input('Segundo aluno: '))
aluno_3 = str(input('Terceiro aluno: '))
aluno_4 = str(input('Quarto aluno: '))

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
shuffle(lista_alunos) # O shuffle não precisa ser atribuído a uma variável, colocamos ele no código e a partir dele a lista está embaralhada.

print(f'A ordem de apresentação será {lista_alunos}')
