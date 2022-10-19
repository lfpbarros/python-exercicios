# Dada a uma lista de entradas de usuário de números inteiros, construa um dicionário com a lista dos valores padrão, a lista dos valores elevados ao quadrado e a lista dos valores elevados ao cubo.

def eleva_numero(lista_de_numeros, numero):
    lista_resposta = []
    for parametro in lista_de_numeros:
        lista_resposta.append(parametro ** numero)
    return lista_resposta

# def cubo(lista_de_numeros):
#     lista_resposta = []
#     for numero in lista_de_numeros:
#         lista_resposta.append(numero ** 3)
#     return lista_resposta

lista_de_valores = []

for valor in range(10): # Repete o for a quantidade de vezes do Range.
    lista_de_valores.append(
        int(input('Fala um número aí: '))
    )

dicionario = {
    'lista padrão': lista_de_valores,
    'lista quadrada': eleva_numero(lista_de_valores, 2),
    'lista cúbica': eleva_numero(lista_de_valores, 3)
}

print(lista_de_valores)

print(dicionario)