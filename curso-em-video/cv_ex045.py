# Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')
jogador = int(input('Qual é a sua jogada? '))
computador = randint(0, 2)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)

# Esse bloco de if poderia ser substituído por uma lista ou tupla e por meio da indexação poderíamos escolher a posição
# itens = ('Pedra', 'Papel', 'Tesoura')
# itens[0]

if jogador == 0:
    mov_jogador = 'Pedra'
elif jogador == 1:
    mov_jogador = 'Papel'
elif jogador == 2:
    mov_jogador = 'Tesoura'

if computador == 0:
    mov_computador = 'Pedra'
elif computador == 1:
    mov_computador = 'Papel'
elif computador == 2:
    mov_computador = 'Tesoura'

print('-=' * 15)
print(f'''Computador jogou {mov_computador}
Jogador jogou {mov_jogador}''')
print('-=' * 15)

# Outra forma de fazer:

# if jogador == computador:
#     print('EMPATE')
# else:
#     if jogador == 0:
#         if computador == 1:
#             print('COMPUTADOR VENCE')
#         elif computador == 2:
#             print('JOGADOR VENCE')
#     elif jogador == 1:
#         if computador == 0:
#             print('JOGADOR VENCE')
#         elif computador == 2:
#             print('COMPUTADOR VENCE')
#     elif jogador == 2:
#         if computador == 0:
#             print('COMPUTADOR VENCE')
#         elif computador == 1:
#             print('JOGADOR VENCE')

if jogador == computador:
    print('EMPATE')
elif jogador == 0 and computador == 1:
    print('COMPUTADOR VENCE')
elif jogador == 0 and computador == 2:
    print('JOGADOR VENCE')
elif jogador == 1 and computador == 0:
    print('JOGADOR VENCE')
elif jogador == 1 and computador == 2:
    print('COMPUTADOR VENCE')
elif jogador == 2 and computador == 0:
    print('COMPUTADOR VENCE')
elif jogador == 2 and computador == 1:
    print('JOGADOR VENCE')
