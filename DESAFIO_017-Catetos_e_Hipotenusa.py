print('=====================DESAFIO_017=====================')
print('''Faça um programa que leia o comprimento do cateto oposto
e do cateto adjacente de um triangulo restângulo.
calcule e mostre o comprimento da hipotenusa\n''')
print ('=====================PROGRAMA======================')
from math import hypot
co=float(input('digite o tamanho do cateto oposto:'))
ca=float(input('digite o tamanho do cateto adjacente' ))
print('O comprimento da hipotenusa é {:.2f}'.format (hypot(co,ca)))