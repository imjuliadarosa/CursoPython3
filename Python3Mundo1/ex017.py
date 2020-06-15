# Desafio 017 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e moste o comprimento da hipotenusa.
from math import hypot
cO = int(input('Informe o comprimento do cateto oposto: '))
cA = int(input('Informe o comprimento do cateto adjacente: '))
h = hypot(cO,cA)
print(f'O comprimento da hipotenusa é igual á {h:.2f}.')