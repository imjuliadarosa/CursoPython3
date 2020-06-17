'''Desafio 027: Faça um programa que leia o nome completo de uma pessoa,
 mostrando em seguida o primeiro e o último nome separadamente.'''
nome = str(input('Informe o nome: ')).strip().upper()
nomeC = nome.split(' ')
print(f'Primeiro nome: {nomeC[0]}\nUltimo nome: {nomeC[len(nomeC)-1]}')