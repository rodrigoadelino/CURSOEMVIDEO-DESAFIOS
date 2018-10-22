print ('==========DESAFIO_062=========')
print ('''Melhore o Desafio 61.
Perguntando para o usuario 
se ele quer mostrar mais alguns 
termos.O Programa encerra quando
ele disser que quer mostrar 0 termo''')
print ('============PROGRAMA===========')
t=int(input('\ndigite o primeiro termo: '))
r=int(input('Digite a razao: '))
termo=t
cont=1
total=0
mais=10
while mais != 0:
      total+=mais
      while cont <= total:
            print('{} '.format(termo),end='')
            termo+=r
            cont+=1
      print ('PAUSE')
      mais=int(input('\n\nQuantos termos voce quer a mais: '))
print('Progressao finalizada com {} termos mostrados'.format (total))



    