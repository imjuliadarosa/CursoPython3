'''Desafio 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
n1 = int(input('Informe o primeiro número: '))
n2 = int(input('Informe o segundo número: '))
n3 = int(input('Informe o terceiro número: '))
nMenor = n3
nMaior = n3
if n1 < n2 and n1 < n3:
    nMenor = n1
if n2<n1 and n2 < n3:
    nMenor = n2
if n1 > n2 and n1 > n3:
    nMaior = n1
if n2 > n1 and n2 > n3:
    nMaior = n2
print(f'O menor número é {nMenor}.')
print(f'O maior número é {nMaior}.')