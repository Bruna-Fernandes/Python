# 06_Faça um programa que pergunte o preço de três produtos e informe qual produto você 
#deve comprar, sabendo que a decisão é sempre pelo mais barato.

p1 = float(input('Qual o valor do primeiro produto?: '))
p2 = float(input('Qual o valor do segundo produto?: '))
p3 = float(input('Qual o valor do terceiro produto?: '))

menor = p1

if (p2 <= p1 and p2 <= p3):
    menor = p2
if (p2 <= p1 and p3 <= p2):
    menor = p3

print('O produto que você deve comprar é: ', menor)