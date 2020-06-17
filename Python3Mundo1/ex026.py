''' Desafio 026 - Faça um programa que leia uma frase
e mostre, quantas vezes a letra A aparece, em qual posição aparece
pela primeira vez, em qual posição aparece pela ultimavez
'''
frase = str(input('Informe a frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes nessa frase \n'
      f'e aparece pela primeira vez na posição {frase.find("A")} \n'
      f'e pela última vez em {frase.rfind("A")}.')
