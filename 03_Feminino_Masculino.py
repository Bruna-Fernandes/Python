# 03_Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = (input('Digite seu sexo sendo: M = masculino e F = feminino. '))
if (sexo == "M"):
    print('Masculino ')
elif (sexo == "F"):
        print('Feminino ')
else:
    print('Sexo informado inválido')
