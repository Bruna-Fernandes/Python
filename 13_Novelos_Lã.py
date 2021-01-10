# 13_Uma confecção produz X blusas de lã e para isto gasta uma certa quantidade de novelos. 
# Faça um algoritmo para calcular quantos novelos de lã ela gasta por blusa.

novelos = float(input('Informe quantidade de novelos: '))
blusas = int(input('Informe a quantidade de blusas: '))
total_novelos = (novelos / blusas)

print('Cada blusa gasta um total de' ,total_novelos,' novelos. ')