# Faça um programa com uma função que dado uma lista e uma posição da mesma faça o quartil dessa posição.
# p_index = int(p * len(lista))
# q1 = 1/4 da lista
# q2 = mediana ✅
# q3 = 3/4 da lista

def quartil(lista):
    lista = sorted(lista)
    posicao_q2 = len(lista) // 2
    if len(lista) % 2 == 0:
        q2 = (lista[posicao_q2 - 1] + lista[posicao_q2]) / 2
    elif len(lista) % 2 == 1:
        q2 = lista[posicao_q2]
    # Primeiramente, é feito o cálculo da mediana, uma lógica é válida para um conjunto com o total de valores
    # par, outra para o conjunto de valores ímpar.
    posicao_q1 = posicao_q2 //2
    # Para calcular a posição do q1, vou atrás da posição da metade da primeira metade da lista.
    q1 = (lista[posicao_q1 - 1] + lista[posicao_q1]) / 2
    posicao_q3 = posicao_q1 + posicao_q2
    # Para calcular a posição do q3, vou atrás da posição da metade da metade final da lista.
    # Que também foi possível de encontrar somando a posição de q1 + posição de q2
    q3 = (lista[posicao_q3] + lista[posicao_q3 + 1]) / 2

    return print(f'Os resultados são: q1:{q1}, q2:{q2} e q3:{q3}.')