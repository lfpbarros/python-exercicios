# Faça um programa que dada a entrada de uma lista o programa calcule a combinatória e nos retorne as combinações em uma nova lista.
# Exemplo de entrada: [1, 2, 3, 4]
# Exemplo de saída: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

lista_inicial = []
numero = 1

while numero != 0:
    numero = int(input('Insira um número na lista (0 para encerrar): '))
    if numero != 0:
        lista_inicial.append(numero)

valores_lista = len(lista_inicial)
# print(valores_lista)
contador = 0
contador_acumulativo = 0
lista_final = []

while contador != (valores_lista + 1):
    for c in range((contador + 1), valores_lista):
        lista_parcial = []
        lista_parcial.append(lista_inicial[contador])
        lista_parcial.append(lista_inicial[c])
        lista_final.append(lista_parcial)
        # print(contador, c)
    contador += 1
print(lista_final)

# Talvez a resolução tenha alguma relação com [x:]