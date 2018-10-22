print ('==========DESAFIO_061=========')
print ('''Refaca o DESAFIO 051 lendo
o primeiro termo e a razao de um PA.
Mostrando os 10 primeiros termos
da progressao usando a estrutura while''')
print ('============PROGRAMA===========')
t=int(input('\ndigite o primeiro termo: '))
r=int(input('Digite a razao: '))
termo=t
cont=1
while cont <=10:
      print('{}->'.format(termo),end='')
      termo+=r
      cont+=1
print ('FIM')