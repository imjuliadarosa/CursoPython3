# Aula 07 - Operadores aritimeticos: +(soma) -(subtração) *( multiplicação)
# /(divisão)  **(potencia) //(divisão inteira) %(resto da divisão)
# ordem de precedencia: 1. () 2. ** 3. * / // % 4. + -
#Desafio 005 - Faça um programa que leia um numero inteiro e mostre seu antecessor e sucessor.
nO = int(input('Informe o número inteiro: '))
nA = nO-1
nS = nO+1
print(f'O antecessor de {nO} é {nA}')
print(f'O sucessor de {nO} é {nS}')
