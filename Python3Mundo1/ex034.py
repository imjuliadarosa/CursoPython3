'''Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
 Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.'''
sal = float(input('Informe o salario atual: '))
if sal > 1250:
    sal = sal + (sal * 0.10)
else:
    sal = sal + (sal * 0.15)
print(f'O novo salario é igual á {sal:.2f} reais.')