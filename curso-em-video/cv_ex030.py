# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numero = int(input('Me diga um número qualquer: '))

if numero % 2 == 0: # Todo número par, tem o resto da divisão por dois como 0.
    print('O número é PAR')
else:
    print('O número é ÍMPAR')
