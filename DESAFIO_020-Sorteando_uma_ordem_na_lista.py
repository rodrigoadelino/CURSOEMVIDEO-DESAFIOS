print('=====================DESAFIO_020=====================')
print('''Um Professor quer sortear a ordem de apresentação 
de trabalhos dos alunos. Faça um programa que leia o nome 
dos quatros alunos e mostre a ordem dos sorteados\n''')
print ('=====================PROGRAMA======================')
from random import shuffle
a=input('Professor digite o nome do 1ºAluno:')
b=input('Professor digite o nome do 2ºAluno:')
c=input('Professor digite o nome do 3ºAluno:')
d=input('Professor digite o nome do 4ºAluno:')
s=[a,b,c,d]
shuffle(s)
print('Professor a ordem dos sorteados é {}'.format(s))
