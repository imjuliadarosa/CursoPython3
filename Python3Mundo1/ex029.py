'''Desafio 029: Escreva um programa que leia a velocidade de um carro.
 Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
  A multa vai custar R$7,00 por cada Km acima do limite.'''
vel = int(input('Informe a velocidade em Km: '))
if vel>80:
    print(f'Você foi multado em {(vel-80)*7} reais.')
else:
    print('Velocidade dentro do limite, prossiga.')