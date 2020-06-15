# Desafio 019 -  Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.
aluno1 = input('Informe o nome do aluno: ')
aluno2 = input('Informe o nome do aluno: ')
aluno3 = input('Informe o nome do aluno: ')
aluno4 = input('Informe o nome do aluno: ')
lista = [aluno1, aluno2, aluno3, aluno4]
from random import choice
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}.')
