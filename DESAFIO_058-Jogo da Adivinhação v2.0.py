print ('=========DESAFIO_058========')
print ('''Melhore o jogo do desafio 
28 onde o computador vai "pensar" 
em numero entre 0 a 10 So que agora
o jogador vai tentar ate advinhar
ate acertar mostrando no final
quantos palpites foram necessários 
para vencer''')
print ('=====================')
from random import randint
palpite=1
ns=randint (0,10)
ne=int(input('Escolha um numero de 0 a 10: '))
if ne == ns:
   print('Parabéns, Voce acertou na primeira tentativa')
while ns != ne:
   if ne < ns:
      print('dica: O numero sorteado e maior')
   if ne > ns:
      print('dica: O número sorteado e menor') 
   palpite=palpite+1
   ne=int(input('Errou escolha outro numero '))
print('\nNumero sorteado foi "{}" Voce Acertou!'.format (ns))
print('Para Acertar voce digitou "{}" numero(s)'.format (palpite))
