# Aula 08 -  Utilizando modulos: import 'allresources' / from 'allresources' import 'oneresource'
# math - ceil, floor, trunc, pow, sqrt, factorial
# ramdom
# Desafio 016 - Crie um programa que leia um número qualquer pelo teclado e mostre na tela sua porção inteira.
# Exemplo - Digite um número: 6.127 / O número 6.127 tem a parte inteira 6.
num = float(input('Digite um número: '))
from math import trunc
numC = trunc(num)
print(f'O numero {num} tem a parte inteira {numC}.')