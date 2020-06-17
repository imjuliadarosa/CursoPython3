'''Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.'''
s1 = float(input('Informe o tamanho do primerio segmento: '))
s2 = float(input('Informe o tamanho do segundo segmento: '))
s3 = float(input('Informe o tamanho do terceiro segmento: '))
if s1<(s2+s3) and s2<(s1+s3) and s3<(s1+s2):
    print('É possivél formar um triangulo com esses segmentos!')
else:
    print('Não é possível formar um segmento com esses segmentos!')