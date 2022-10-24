# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida

peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = peso / (altura ** 2)

print(f'O IMC dessa pessoa é de {imc:.1f}')

if imc < 18.5:
    print('Você está ABAIXO DO PESO normal!')
elif imc >= 18.5 and imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO')
elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')
elif imc >= 40:
    print('Você está com OBESIDADE MÓRBIDA, cuidado!')

