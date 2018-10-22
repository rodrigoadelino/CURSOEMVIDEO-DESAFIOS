print('================DESAFIO_035===================')
print('''Desenvolva um programa que leia o comprimento de tres
retas e diga ao usuario se elas podem ou não formar um triângulo.''')
print('================PROGRAMA=>==================')
a=float(input('Digite o comprimento da primeira reta: '))
b=float(input('Digite o comprimento da segunda  reta: '))
c=float(input('Digite o comprimento da terceira reta: '))
if a<b+c and b<a+c and c<a+b:
   print('Sim é possivel formar um triagulo')
else:
   print('Não é possivel formar um triangulo')