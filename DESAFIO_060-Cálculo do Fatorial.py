print('=====DESAFIO 060=====')
print('''Faca um programa que leia
um numero qualquer 
E mostre o seu fatorial
Ex: 5!=5X4X3X2X1=120''')

#from math import factorial
#n=int(input('Digite um numero para ver seu fatorial: '))
#while n>0:
#f=factorial (n)
#print ('{}!={}'.format (n,f))



n=int(input('\nDigite o número: '))
c = n
f = 1
print('calculando {}!='.format (n), end='')
while c > 0:
      print ('{}'.format (c), end='')
      print (' x ' if c>1 else ' = ', end='')
      f *= c
      c -= 1
print(f)