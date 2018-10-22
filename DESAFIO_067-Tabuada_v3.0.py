print('=====================DESAFIO_067=======================')
print('''Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado 
for negativo. ''')
print('======================PROGRAMA=======================')
while True:
    n=int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        break
    for c in range (0,11):
        print ('{} X {} = {}'.format(n,c,(c*n)))
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')