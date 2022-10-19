# Faça um programa para a leitura de duas notas parciais de um aluno. O programa calcula a média e apresenta:
# Aprovado se a média for maior ou igual a 7
# Reprovado se a média for menor que 7
# Aprovado com distinção se a média for igual a dez.

nome = str(input('Nome do aluno(a): '))
parcial_1 = float(input('Insira a nota do primeiro semestre: '))
parcial_2 = float(input('Insira a nota do segundo semestre: '))

media = (parcial_1 + parcial_2) / 2

if media == 10:
    print(f'{nome} foi aprovado(a) com distinção! Parabéns! Você é nota 10!! ')
elif media >= 7:
    print(f'{nome} foi aprovado(a) com a média de {media}. Parabéns!!!')
elif media < 7:
    print(f'{nome} foi reprovado(a) com média {media}, você precisa estudar mais...')
else:
    print('Algo está incorreto, tente novamente.')
