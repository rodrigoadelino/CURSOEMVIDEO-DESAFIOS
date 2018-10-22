print('================DESAFIO_031===================')
print('''Desenvolva um programa que pergunte a distancia
de uma viagem em km.Calcule o preço da passagem,
cobrando R$ 050 por Km para viagens de até 200Km
e R$ 0,45 para viagens mais longas''')
print('================PROGRAMA===================')
viagem=int(input('Qual a distancia da viagem?: '))
if viagem <= 200:
    print('A viagem custara R${:.2f}'.format(viagem*0.50))
elif viagem> 200:
    print('A viagem custara R${:.2f}'.format(viagem*0.45))