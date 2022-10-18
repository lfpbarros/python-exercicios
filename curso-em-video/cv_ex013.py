# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input('Qual é o salário do funcionário? R$'))
aumento = salario * 15/100 # Ou salario * 0.15
novo_salario = salario + aumento
print(f'Um salário que ganhava R${salario}, com 15% de aumento, passa a receber R${novo_salario:.2f}')
