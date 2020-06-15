# desafio 012 - leia preço e mostre com 5% de desconto
preco = float(input('Informe o preço: '))
novoPreco = preco-(preco*0.05)
#novoPreco = preco - (preco * 5 / 100)
print(f'O preço original é {preco} e o novo preço com o percentual de 5% de desconto é igual á {novoPreco}.')