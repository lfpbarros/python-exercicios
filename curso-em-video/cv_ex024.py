# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Em que cidade você nasceu? ')).strip().lower()
separado = cidade.split()
print(separado[0] == 'santo')

# Lógica do professor Guanabara

# print(cidade[:5] == 'santo')
