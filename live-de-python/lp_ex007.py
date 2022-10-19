# Faça um programa que receba uma string e responsa se ela tem alguma vogal, se sim, quais são? E também diga se ela é uma frase ou não.

from operator import index


texto = str(input('Insira algum texto: ')).strip().lower()

vogais = ''
vogal = False

if 'a' in texto:
    vogais += 'a, '
    vogal = True
if 'e' in texto:
    vogais += 'e, '
    vogal = True
if 'i' in texto:
    vogais += 'i, '
    vogal = True
if 'o' in texto:
    vogais += 'o, '
    vogal = True
if 'u' in texto:
    vogais += 'u, '
    vogal = True

if vogal is True:
    print(f'A string possui vogais. As disponíveis são as seguintes: {vogais[:-2]}.') # Utilizando o fatiamento de strings é possível remover alguns valores indesejados.
else:
    print('A string não possui vogais. ')

frase = texto.find(' ') # Quando o find não encontra o caracter, ele retorna -1.

if frase > 0:
    print('Essa string é uma frase.')
else:
    print('Essa string não é uma frase. ')