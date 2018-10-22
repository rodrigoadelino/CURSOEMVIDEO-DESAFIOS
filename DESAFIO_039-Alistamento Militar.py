print('=====================DESAFIO_039=====================')
print('''Faça um programa que leia o ano de nascimento de um jovem e infome,
de acordo com sua idade, se ele ainda vai se alistar ao servico militar,
se é a hora de se alistar ou se ja passou do tempo do alistamento.
Seu programa tambem devera quanto tempoque falta ou que passou do prazo''')
print ('=====================PROGRAMA=======================')
from datetime import date
atual=date.today().year
nasc=int(input('Em qual ano você nasceu: '))
idade = atual - nasc
print('Quem Nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade==18:
   print('Você tem que se alistar IMEDIATAMENTE!')
elif idade<18:
   saldo=18-idade
   print('Ainda faltam {} anos para o alistamento'.format(saldo))
   ano=atual + saldo
   print('Seu alistamento será em {}'.format(ano))
elif idade>18:
   saldo = idade - 18
   print ('Você ja deveria ter se alistado há {} ano(s)'.format(saldo))
   ano=atual-saldo
   print('Seu alistamento foi em {}'.format(ano))
