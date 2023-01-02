# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

n_aleatorio = randint(0, 10)
acertou = False
tentativas = 0

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar... ')
print('-=-' * 20)

while not acertou:
    tentativas += 1
    n_tentativa = int(input('Em que número eu pensei? '))
    if n_tentativa == n_aleatorio:
        acertou = True
    else:
        print('O número que pensei não é esse... Tente novamente!')

print(f'PARABÉNS! Você conseguiu acertar após {tentativas} tentativas.')
