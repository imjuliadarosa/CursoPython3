'''Desafio 036: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
 Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
casa = float(input('Informe o valor da casa: '))
salario = float(input('Informe seu salario: '))
anos = int(input('Informe em quantos anos pretende pagar: '))
if casa/(anos*12)>(salario*0.3):
    print('Infelizmente não é possivél fazer o financiamento.')
else:
    print('Emprestimo autorizado!')