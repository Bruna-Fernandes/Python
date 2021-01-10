# 14_A fábrica de refrigerantes Meia-Cola vende seu produto em três formatos: 
# lata de 350 ml, garrafa de 600 ml e garrafa de 2 litros. 
# Se um comerciante compra uma determinada quantidade de cada formato. 
# Faça um algoritmo para calcular quantos litros de refrigerante ele comprou.

lata = int(input('Informe a quantidade de latas de 350 ml: '))
garrafa1 = int(input('Informe a quantidade garrafas de 600 ml: '))
garrafa2 = int(input('Informe a quantidade garrafas de 2 litros: '))
total_litros = ((lata * 350) + (garrafa1 * 600) + (garrafa2 * 2000))

print('O total da compra em litros foi de: %.f '% (total_litros))

