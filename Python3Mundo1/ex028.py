'''Aula 10 - Condições Simples e Compostas
if : else:
print('Isso'if aquilo<=3 else 'aquilo)
Desafio 028: Escreva um programa que faça o computador “pensar”
 em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
 qual foi o número escolhido pelo computador.
 O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''
from random import randint
num = randint(0,5)
numA = int(input('Vou pensar em um número de 0 á 5. Advinhe o número que estou pensando! '))
if num==numA:
    print('Parabéns, pensamos no mesmo número!')
else:
    print(f'Infelizmente o numero que você advinhou não foi {num}. Tente novamente')