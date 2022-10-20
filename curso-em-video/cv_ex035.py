# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 15)
print('Analisador de Triângulos')
print('-=-' * 15)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

# A regra de condição de existência de triângulos é: a soma das retas opostas deve ser maior do que a reta escolhida.
# Ex.: R1 precisa ser menor que a soma de R2 e R3.

if (r2 + r3) > r1 and (r1 + r3) > r2 and (r1 + r2) > r3:
    print('Os segmentos acima PODEM FORMAR triângulo. ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo. ')
