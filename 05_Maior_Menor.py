# 05_Faça um Programa que leia três números e mostre o maior e o menor deles.

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

print('O maior número foi: ', maior , 'e o menor foi: ', menor)
