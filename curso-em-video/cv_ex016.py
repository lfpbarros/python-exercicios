# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc # Função da biblioteca math que retorna apenas a porção inteira

valor = float(input('Digite um valor: '))
print(f'O valor digitado foi {valor} e a sua porção inteira é {trunc(valor)}')

# Também podemos resolver esse programa usando a função int().
