# Faça um programa com uma função que calcule a dispersão de uma lista.
# Funções embutidas que podem ajudar:
# min(lista) -> retorna o menor valor
# max(lista) -> retorna o maior valor
# Amplitude = valor máximo - valor mínimo
# Primeiro, se calcula a média aritmética da lista, depois o desvio(cada módulo menos a média). Os valores precisam ser positivos.
# Desvio médio é a média aritmética dos desvios
# Variância é média do quadrado de cada desvio
# Desvio padrão é a raiz quadrada da variância

# Para calcular raiz quadrada: x ** (1/2)

def dispersao(lista):
    minimo = min(lista)
    maximo = max(lista)
    amplitude = maximo - minimo
    media_aritmetica = sum(lista) / len(lista)
    desvio = []
    for modulo in lista:
        valor_desvio = modulo - media_aritmetica
        if valor_desvio < 0:
            valor_desvio = valor_desvio * -1
        desvio.append(valor_desvio)
    desvio_medio = sum(desvio) / len(desvio)
    lista_variancia = []
    for modulo in desvio:
        valor_variancia = modulo ** 2
        lista_variancia.append(valor_variancia)
    variancia = sum(lista_variancia) / len(lista_variancia)
    desvio_padrao = variancia ** (1/2)
    return print(f'''Os valores são: amplitude = {amplitude}, desvio médio = {desvio_medio},
    variância = {variancia} e desvio padrão = {desvio_padrao:.3}.''')