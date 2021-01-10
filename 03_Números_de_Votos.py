# 03_Numa eleição existem três candidatos. Faça um programa que peça o número 
# total de eleitores. Peça para cada eleitor votar e ao final mostrar o número 
# de votos de cada candidato.

candidato1=0
candidato2=0
candidato3=0

quantos = int(input('Informe quantos eleitores: '))
for i in range(quantos):
  print('Eleitor ',i+1, ' (faltam ',quantos-i,')')
  voto = input('Informe seu voto : 1 ou 2 ou 3?')
  if voto == '1': candidato1 = candidato1+1
  if voto == '2': candidato2 = candidato2+1
  if voto == '3': candidato3 = candidato3+1

print('O candidato A teve ',candidato1, 'votos')
print('O candidato B teve ',candidato2, 'votos')
print('O candidato C teve ',candidato3, 'votos')
