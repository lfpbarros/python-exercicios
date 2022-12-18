# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('=' * 25)
print('{:^25}'.format('10 TERMOS DE UMA PA')) # o :^25 centraliza o valor nessa quantidade de espaços
print('=' * 25)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
# décimo termo de uma pa: primeiro + (10 - 1) * razão

print('{}'.format(termo), end=' -> ')

for i in range(9):
    termo += razao
    print(f'{termo}', end=' -> ')

print('ACABOU')