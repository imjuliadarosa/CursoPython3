'''Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é bissexto.'''
ano = int(input('Para analizar o ano atual informa 0. Informe o ano: '))
if ano==0:
    from datetime import date
    ano = date.today().year
if ano%4==0 and ano%100!=0 or ano%400==0:
    print('Ano é bissexto.')
else:
    print('Ano não é bissexto.')