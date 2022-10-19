# Faça um programa que dada a entrada de uma lista ele faça o cálculo acumulativo da mesma:
# Exemplo de entrada: [1, 2, 3, 4]
# Exemplo de saída: [1, 3, 6, 10]

lista = []
numero = 1

while numero != 0:
    numero = int(input('Insira um número na lista, para encerrar digite 0: '))
    if numero != 0:
        lista.append(numero)

lista_acumulativa = []
valor_acumulativo = 0

for item in lista:
    valor_acumulativo += item
    lista_acumulativa.append(valor_acumulativo)
print(lista_acumulativa)

