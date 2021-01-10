# 04_O restaurante a quilo Bem-Bão cobra R$12,00 por cada quilo de refeição. Escreva um
# algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor
# a pagar. Assuma que a balança já desconte o peso do prato.

peso = float(input('Informe o peso do prato: '))

pesokg = 12.00
valor = peso * pesokg

print('O valor a pagar é R$:',valor)