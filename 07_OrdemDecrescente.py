# 07_Faça um Programa que leia três números e mostre-os em ordem decrescente.

p1 = int(input('Digite o primeiro número: '))
p2 = int(input('Digite o segundo número: '))
p3 = int(input('Digite o terceiro número: '))

if(p3 > p2):
    p = p3
    p3 = p2
    p2 = p

if(p2 > p1):
    p = p2
    p2 = p1
    p1 = p

if(p3 > p2):
    p = p3
    p3 = p2
    p2 = p

print(p1,'-',p2,'-',p3)
