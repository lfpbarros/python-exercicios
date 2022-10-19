# Baseando-se nos exercícios passados, monte um dicionário com as seguintes chaves:
# lista, somatório, tamanho, maior valor e menor valor

def soma(lista_de_valores):
    return(sum(lista_de_valores))

def tamanho(lista_de_valores):
    return(len(lista_de_valores))

def maior(lista_de_valores):
    return(max(lista_de_valores))

def menor(lista_de_valores):
    return(min(lista_de_valores))

lista = []
while True:
    valor = int(input('Insira um número na lista: [Para encerrar 0] '))    
    if valor == 0:
        break
    else:
        lista.append(valor)

dicionario = {
    'lista': lista,
    'somatório': soma(lista),
    'tamanho': tamanho(lista),
    'maior valor': maior(lista),
    'menor valor': menor(lista)
}

print(dicionario)