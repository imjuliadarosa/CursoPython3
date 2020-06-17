"""Aula 9 - Manipulação de cadeia de texto.
Fatiamento. str[xbegin:xend:xjump]
Análise. str.len()==length
Transformação. str.replace() str.upper() str.lower() str.capitalize()
 str.tittle() str.strip() str.rstrip() str.lstrip()
 Divisão. str.split()
 Junção. '-'.join(str)"""
# Desafio 022 - Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todos as letras maiusculas
# O nome com todas as letras minusculas
# quantas letras ao tod, sem considerar espaços
# Quantas letras tem o primerio nome
nome = str(input('Informe nome: ')).strip()
print(f'Seu nome em letras maiusculas: {nome.upper()}')
print(f'Seu nome em letras minusculas: {nome.lower()}')
print(f'Seu nome tem {len(nome)-nome.count(" ")} letras.')
nomeC = nome.split()
print(f'Seu primeiro nome é {nomeC[0]} e tem {len(nomeC[0])} letras.')