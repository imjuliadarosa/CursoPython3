'''Desafio 024 - crie um programa que leia o nome de uma cidade
 e diga se ela começa ou não com o nome santo'''
cidade = input('Informe o nome da cidade: ')
print(f'A cidade começa Santo no nome? {cidade[:5].upper == "SANTO"}.')