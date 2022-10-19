# Faça um programa com uma função que calcula a mediana de uma lista.
# Funções embutidas que podem ajudar:
# sorted(lista) -> ordena a lista.

def mediana(lista):
    lista = sorted(lista)
    if len(lista) % 2 == 0:
        posicao = len(lista) // 2
        numero_mediana = (lista[posicao - 1] + lista[posicao]) / 2
    elif len(lista) % 2 == 1:
        posicao = len(lista) // 2
        numero_mediana = lista[posicao]
    return f'O resultado da mediana é {numero_mediana}'