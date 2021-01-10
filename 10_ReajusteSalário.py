# 10_Uma empresa resolveu dar um aumento de salário aos seus colaboradores e lhe
# contrataram para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o
# seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

salario = float(input('Salário do colaborador: '))

if (salario <= 280):
    porcentagem = 20
elif (salario <= 700):
    porcentagem = 15
elif (salario <= 1500):
    porcentagem = 10
else:
    porcentagem = 5

print('Salario original: R$ ', salario)
print('Porcentagem: ', porcentagem, '%')

porcentagem = porcentagem/100.0
aumento = porcentagem * salario
novo_salario = salario + aumento

print('Aumento: R$ ', aumento)
print('Novo salário: R$ ', novo_salario)
