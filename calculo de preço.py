import math

while True:
    pc = float(input('Digite o preço de custo do produto: '))
    lc = float(input('Qual a porcentagem de lucro que você quer? (Digite apenas números): '))
    sub_total = lc / 100
    nsbt = 1 - sub_total
    preco_final = pc / nsbt
    print ('Preço do produto deverá ser: ', math.ceil(preco_final))
    print ("")
