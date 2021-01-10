# 06_Uma fábrica controla o tempo de trabalho sem acidentes pela quantidade de dias.
# Faça um algoritmo para converter este tempo em anos, meses e dias. Assuma que cada
# mês possui sempre 30 dias.

Qt = int(input('Informe a quantidade de dias sem acidentes: '))
Anos = Qt/360
Meses = (Qt % 360) / 30
Dias = (Qt % 360) % 30

print('Ano(s): %.f ' % (Anos))
print('Mes(es): %.f ' % (Meses))
print('Dia(s): %.f ' % (Dias))


