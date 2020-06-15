# Desafio 011 - leia a altura e largura de uma parede em metros, calcule sua area e quantidade de tinta necessaria
#para pintar a parede, um litro de tinta pinta 2m².
altura = float(input('Informe a altura da parede em metros: '))
largura = float(input('Informe a largura da parede em metros: '))
area = altura*largura
litrosTinta = area/2
print(f'A parede mede {altura} metros de altura e {largura} metros de largura, sua area é igual á {area} m² '
      f'e é necessario {litrosTinta} para pintar toda a area da parede.')