print('=====================DESAFIO_068=======================')
print('''Faca um programa que jogue par ou impar com o computador
O jogo só sera interrompido  quando o jogador PERDER.Mostrando
o total de vitorias consecutivas que ele conquistou no final do jogo. ''')
print('======================PROGRAMA=======================')
print('='*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('='*25)
from random import randint
v=0
resu=''
while True:
   n=int(input('Digite um valor: '))
   tipo=str(input('Par ou impar? [P/I]: ')) .upper().strip()[0]
   c=randint(0,10)
   total = n + c
   if total%2==0:
      resu='PAR'
   else:
      resu='IMPAR'
   while tipo not in 'PI':
         tipo=str(input('Par ou impar? [P/I]: ')) .upper().strip()[0] 
   print('='*25)
   print('Voce jogou {} e o computador {} Total de {} Deu {}'.format (n, c, total,resu))
   print('='*25)
   if tipo == 'P':
      if total%2 == 0:
         print('Você VENCEU!')
         v += 1
      else:
         print('Você PERDEU!')
         break
   elif tipo =='I':
      if total%2 == 1:
         print('Você VENCEU!')
         v += 1
      else:
         print('Você PERDEU!')
         break
   print('Vamos jogar novamente...')
   print('='*25)
print ('GAME OVER! Você venceu {} vezes'.format(v))
