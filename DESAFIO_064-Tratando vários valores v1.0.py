print('=======DESAFIO_064======')
print('''Crie um programa que leia 
vários números inteiros 
pelo teclado. O programa só vai 
parar quando o usuário digitar 
o valor 999, que é a condição
de parada. No final, mostre 
quantos números foram digitados
e qual foi a soma entre eles 
(desconsiderando o flag)''')
print('========PROGRAMA========')

n=int(input('digite um numero: '))
cont=0
soma=0
for c in range (n):
    while n!= 999:
          soma+=n
          n=int(input('digite outro número: '))
          cont+=1
print ('\nforam digitados {} numero(s)'.format(cont))
print ('A soma dos numeros digitados é {}'.format(soma))