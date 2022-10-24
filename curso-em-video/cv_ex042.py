# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    if r1 != r2 != r3 != r1:
        tipo = 'ESCALENO'
    elif r1 == r2 == r3: # Outra forma de fazer: r1 == r2 and r2 == r3
        tipo = 'EQUILÁTERO'
    elif r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r1: # Nesse caso, poderia ser usado o else.
        tipo = 'ISÓSCELES'
    print(f'Os segmentos acima PODEM FORMAR um triângulo {tipo}!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo! ')
