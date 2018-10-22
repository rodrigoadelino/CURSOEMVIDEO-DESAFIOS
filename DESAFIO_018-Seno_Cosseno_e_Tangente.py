print('=====================DESAFIO_018=====================')
print('''Faça um programa que leia um ângulo qualquer e mostre 
na tela o valor do seno, cosseno e tangente desse ângulo \n''')
print ('=====================PROGRAMA======================')
from math import sin,cos,tan,radians
a=float(input('Digite um ângulo: '))
s=sin(radians(a))
c=cos(radians(a))
t=tan(radians(a))
print('O agulo digitado tem o SENO de: {:.2f}\nO agulo digitado tem o COSSENO de: {:.2f}\nO agulo digitado tem a TANGENTE de:{:.2f}'.format(s, c,t))