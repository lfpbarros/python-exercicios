# Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

nascimento = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year

idade = ano_atual - nascimento

print(f'Quem nasceu em {nascimento} tem {idade} anos em {ano_atual}.')

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade > 18:
    tempo_de_alistamento = idade - 18
    ano_alistamento = ano_atual - tempo_de_alistamento
    print(f'Você já deveria ter se alistado há {tempo_de_alistamento} anos.')
    print(f'Seu alistamento foi em {ano_alistamento}.')
elif idade < 18:
    tempo_para_alistamento = 18 - idade
    ano_alistamento = ano_atual + tempo_para_alistamento
    print(f'Ainda faltam {tempo_para_alistamento} anos para o alistamento.')
    print(f'Seu alistamento será em {ano_alistamento}.')
