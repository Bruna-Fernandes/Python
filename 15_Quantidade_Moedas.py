# 15_Pedrinho tem um cofrinho com muitas moedas, e deseja saber quantos reais
# conseguiu poupar. Faça um algoritmo para ler a quantidade de cada tipo de moeda,
# e imprimir o valor total economizado, em reais. Considere que existam moedas 
# de 1, 5, 10, 25 e 50 centavos, e ainda moedas de 1 real. 
# Não havendo moeda de um tipo, a quantidade respectiva é zero.

um_centavo = int(input('Informe a quantidade de moedas de 1 centavo: '))
cinco_centavos = int(input('Informe a quantidade de moedas de 5 centavos: '))
dez_centavos = int(input('Informe a quantidade de moedas de 10 centavos: '))
vinte_cinco_centavos = int(input('Informe a quantidade de moedas de 25 centavos: '))
cinquenta_centavos = int(input('Informe a quantidade de moedas de 50 centavos: '))
um_real = int(input('Informe a quantidade de moedas de 1 real: '))

v1 = um_centavo * 0.01
v2 = cinco_centavos * 0.05
v3 = dez_centavos * 0.10
v4 = vinte_cinco_centavos * 0.25
v5 = cinquenta_centavos * 0.50
v6 = um_real * 1.00

print('O valor total economizado foi: R$', v1 + v2 + v3 + v4 + v5 + v6)
