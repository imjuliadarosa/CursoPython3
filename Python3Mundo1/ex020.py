# Desafio 020 - O mesmo professor do desafio anterior que sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a oredem sorteada.
n1 = input('Informe o nome do aluno: ')
n2 = input('Informe o nome do aluno: ')
n3 = input('Informe o nome do aluno: ')
n4 = input('Informe o nome do aluno: ')
lista = [n1, n2,n3,n4]
from random import shuffle
shuffle(lista)
print(f'A ordem de apresentação será {lista}.')