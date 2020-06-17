'''Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em Km.
 Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''
km = int(input('Informe os km da viagem: '))
preco = km*0.50 if km<=200 else km*0.45
print(f'Sua passagem custará {preco} reais.')