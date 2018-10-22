print('================DESAFIO_029====================')
print('''Pergunte ao usuario a velocidade do carro dele
Se ele ultrapassar 80km/h, mostre uma mensagem 
dizendo que ele foi multado. A multa vai custar 
R$7,00 para cada Km acima do limite de velocidade ''')
print('=================PROGRAMA==================')
v=int(input('Informe a velocidade que estava dirigindo: '))
if v <=80:
   print('Parabens você nao foi multado')
#print('Voce estava dirigindo a {}Km/h'.format((v)))
else:
   print('Você foi multado')
   print('Voce estava dirigindo a {}Km/h'.format (v))
   print('O valor da multa é de R$ 7,00 po cada Km/h acima do permitido')
   print('O valor da multa será de R$',((v-80)*7))


