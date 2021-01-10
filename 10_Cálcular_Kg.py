# 10_A lanchonete Gostosura vende apenas um tipo de sanduíche, cujo recheio inclui
# duas fatias de queijo, uma fatia de presunto e uma rodela de hambúrguer. Sabendo
# que cada fatia de queijo ou presunto pesa 50 gramas, e que a rodela de hambúrguer
# pesa 100 gramas, faça um algoritmo em que o dono forneça a quantidade de
# sanduíches a fazer, e a máquina informe as quantidades (em quilos) de queijo, presunto
# e carne necessários para compra.

sanduiches = int(input('Informe a quantidade de sanduíches: '))
queijo = 100 * sanduiches
presunto = 50 * sanduiches
carne = 100 * sanduiches

print('A quantidade necessária de queijo é: ', queijo,'g')
print('A quantidade necessária de presunto é: ', presunto,'g')
print('A quantidade necessária de carne é: ', carne,'g')
