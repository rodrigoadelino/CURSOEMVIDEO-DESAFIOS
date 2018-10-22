print('=====================DESAFIO_045=====================')
print('''Crie um programa que faça o computador jogar Jokenpô com você.''')
print ('=====================PROGRAMA======================')
print('''Suas opções:
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA''')
from random import randint
from time import sleep
itens=('PEDRA', 'PAPEL','TESOURA')
c = randint(0,2)
p=int(input('\nEscolha sua Opção: '))
#if p >2:
#  print('Opção inválida')
#   p=(int(input('\nEscolha sua Opção: '))
#else:   
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('\nVoce escolheu {}'.format(itens[p]))
print('O Computador escolheu {}'.format(itens[c]))
if p==c:
   print('\nDeu empate')
elif p==0 and c==2 or p==2 and c==1 or p==1 and c==0:
   print('\nVocẽ venceu!!!')
else:
   print ('\nO computador Venceu!!!')