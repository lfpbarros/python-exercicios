# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex.: 1834
# Unidade: 4, dezena: 3, centena: 8, milhar: 1

# Fazendo com tratamento de string

# n = str(input('Informe um número: ')).strip()
# print(f'Analisando o número {n}')
# n = '000' + n
# print(f'Unidade: {n[-1]}')
# print(f'Dezena: {n[-2]}')
# print(f'Centena: {n[-3]}')
# print(f'Milhar: {n[-4]}')

# Fazendo com matemática

n = int(input('Informe um número: '))
milhar = n // 1000
resto = n - milhar * 1000
centena = resto // 100
resto = resto - centena * 100
dezena = resto // 10
resto = resto - dezena * 10
unidade = resto
print(f'Analisando o número {n}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')

# Explicação do professor Guanabara para o fatiamento:

# u = n // 1 % 10
# d = n // 10 % 10
# c = n // 100 % 10
# m = n // 1000 % 10