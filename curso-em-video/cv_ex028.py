# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar... ')
print('-=-' * 20)
numero = randint(0, 5) # O computador sorteia um inteiro entre 0 e 5
palpite = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
if numero == palpite:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {numero} e não no {palpite}!')
