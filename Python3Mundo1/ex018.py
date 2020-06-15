# Desafio 018 - Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
ang = int(input('Informe o ângulo: '))
from math import radians,sin, cos, tan
sin = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print(f'Seno é igual á {sin:.2f}. \n Cosseno é igual a {cos:.2f}. \n Tangente é igual á {tan:.2f}.')