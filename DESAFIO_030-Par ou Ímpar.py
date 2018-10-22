print('================DESAFIO_030===================')
print('''Crie um programa que leia um numero interio
q mostre na tela se ele é PAR ou IMPAR''')
print('================PROGRAMA===================')
n1=int(input('Digite o primeiro número: '))
if n1 == 0:
   print('zero é neutro')
elif n1//1%10==2 or n1//1%10==4 or n1//1%10==0 or n1//1%10==6 or n1//1%10==8:
     print('o numero digitado é par')
else:
     print('o numero digitado é impar')
