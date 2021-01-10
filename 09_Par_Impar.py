# 09_Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
# Dica: utilize o operador módulo (resto da divisão).

n1 = int(input('Digite um número: '))

if (n1%2) == 0:
  print("Par")
else:
  print("Ímpar")