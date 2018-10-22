print('''======DESAFIO_063=====''')
print ('''Escreva um programa que leia 
um número n inteiro qualquer e
mostre na tela os n primeiros
elementos de uma sequência de 
Fibonacci.Ex:
0 -> 1 ->1 ->2 ->3 ->5 ->8''')
print('''=======PROGRAMA=======''')
n=int(input('Quantos termos você quer mostrar? '))
print ('='*30)
t1=0
t2=1
cont=3
print('{} ->{} ->'.format(t1,t2), end='')
while cont <=n:
      t3= t1 + t2
      print('{} ->'.format(t3), end ='')
      cont+=1
      t1=t2
      t2=t3      
print ('FIM')#while t > t2:
      