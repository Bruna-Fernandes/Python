# 04_Faça um programa que, dado um conjunto de N números, determine o menor valor, 
# o maior valor e a soma dos valores.
print ('Digite três números ')
n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
n3 = int(input('Digite terceiro número: '))

maior = n1
if (n2>= n1 and n2 >= n3):
    maior = n2
if (n3 >= n1 and n3 >= n2):
    maior = n3

menor = n1
if (n2 <= n1 and n2 <= n3):
    menor = n2
if (n2 <= n1 and n3 <= n2):
    menor = n3

print('O maior número foi: ', maior)
print('O menor número foi: ', menor)
print('A soma dos valores é: ',maior + menor)