# 11_A empresa Hipotheticus paga R$10,00 por hora normal trabalhada, e R$15,00 
# por hora extra. Faça um algoritmo para calcular e imprimir o salário bruto e o
# salário líquido de um determinado funcionário. Considere que o salário
# líquido é igual ao salário bruto descontando-se 10% de impostos.

h = int(input('Informe a quantidade de horas trabalhadas: '))
h_extra = int(input('Informe a quantidade de horas extras: '))
valor_h = 10.00
valor_h_extra = 15.00
s_bruto = (h * valor_h) + (h_extra * valor_h_extra)
s_liquido = (s_bruto * 10)/100
valor_s_liquido = (s_bruto - s_liquido)

print('O salário bruto é: %.2f '% (s_bruto))
print('O salário líquido é: %.2f '% (valor_s_liquido))
