# Faça um programa que itera em uma string e toda vez que uma vogal aparecer na sua string print o seu nome entre as letras.

palavra = 'abracadabra'
vogais = 'aeiou'

# for letra in palavra:
#     if letra == 'a':
#         print('Luis')
#     elif letra == 'e':
#         print('Luis')
#     elif letra == 'i':
#         print('Luis')
#     elif letra == 'o':
#         print('Luis')
#     elif letra == 'u':
#         print('Luis')
#     else:
#         print(letra)

for letra in palavra:
    if letra in vogais:
        print('Luis')
    else:
        print(letra)