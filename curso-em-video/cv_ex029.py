# Escreva um programa que leia a velociadade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7.00 por cada km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
limite = 80

if velocidade > limite:
    multa = (velocidade - limite) * 7
    print('MULTADO! Você excedeu o limite permitido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${multa:.2f}!')

print('Tenha um bom dia! Dirija com segurança! ')
