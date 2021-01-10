# 07_Faça um algoritmo para ler o salário de um funcionário e aumentá-Io em 15%.
#  Após o aumento, desconte 8% de impostos. Imprima o salário inicial, o salário
#  com o aumento e o salário final.

salario = float(input('Salário do colaborador: '))

aumento = (salario * 15)/100
salario_aumento = (aumento + salario)
desconto = (salario_aumento - 8)/100
salario_final = (salario_aumento - desconto)

print('Salário Inicial: %.2f ' % (salario))
print('Salário com aumento: R$ %.2f ' % (salario_aumento))
print('Salário final: R$ %.2f ' % (salario_final))