# 03_A padaria Hotpão vende uma certa quantidade de pães franceses e uma quantidade
# de broas a cada dia. Cada pãozinho custa R$ 0,12 e a broa custa R$ 1,50. 
# Ao final do dia, o dono quer saber quanto arrecadou com a venda dos pães e broas (juntos), e
# quanto deve guardar numa conta de poupança (10% do total arrecadado). 
# Você foi contratado para fazer os cálculos para o dono. Com base nestes fatos, 
# faça um algoritmo para ler as quantidades de pães e de broas, e depois calcular os dados
# solicitados.

paes = int(input('Informe a quantidade de pães vendidos: '))
broas = int(input('Informe a quantidade de broas vendidas: '))

vp = paes * 0.12
vb = broas * 1.50
total = float(vp + vb)
porc = float(10/100 * total)

print('O valor total arrecadado foi R$',total)
print('O valor a ser guardado deve ser: ',porc)