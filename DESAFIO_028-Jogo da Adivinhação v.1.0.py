print('=====================DESAFIO_028=====================')
print('''Escreva um programa que faça o computador "pensar" 
em um número Inteiro entre 0 e 5 e peça para o usuario tentar 
descobrir qual foi o numero escolhindo pelo computador. 
O Programa deverá escrever na tela se o usuario venceu
ou perdeu.\n''')
print ('=====================PROGRAMA======================')
from random import randint
ns=randint (0,1)
ne=int(input('Escolha um numero de 0 a 5: '))
print('voce escolheu o numero {} '.format(ne))
print('O numero sorteado foi {} '.format(ns))
if ne == ns:
    print('Parabens voce acertou')
else:
    print('Infelizmente voce errou')

