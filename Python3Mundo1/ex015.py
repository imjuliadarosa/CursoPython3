#Exercício Python 015: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa
# R$60 por dia e R$0,15 por Km rodado.
kmP = float(input('Informe km percorridos: '))
dias = int(input('Informe dias de aluguel: '))
preco = (60*dias)+(kmP*0.15)
print(f'O carro foi alugado por {dias} dias e rodou {kmP} km, o valor a ser pago é {preco}')