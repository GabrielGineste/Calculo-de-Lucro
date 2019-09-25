import math

while True:
    custop = float(input('Digite o preço de custo do produto: '))
    preco = (custop / 0.75)
    round(preco, 1)
    print ('Preço do produto deverá ser: ', math.ceil(preco))
    print ("")
