print('=====================DESAFIO_023=====================')
print('''Faca um programa que leia
um número de 0 a 9999 e mostre na tela 
cada um dos dígitos separados
\n''')
print ('=====================PROGRAMA======================')

n=int (input('Digite um número de 0 a 9999: '))
uni = n // 1 % 10
dez = n // 10 % 10
cen = n // 100 % 10
mil = n // 1000 % 10
print('unidade: ',(uni))
print('dezena : ',(dez))
print('centena: ',(cen))
print('milhar : ',(mil))









