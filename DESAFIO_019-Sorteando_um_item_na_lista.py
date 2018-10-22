print('=====================DESAFIO_019=====================')
print('''Um Professor quer sortear um dos seus quatro alunos
para apagar o quadro.Faça um programa que ajude ele lendo 
o nome dos alunos e escrevendo o nome do escolhido\n''')
print ('=====================PROGRAMA======================')

from random import choice
a=input('Professor digite o Nome do 1ºAluno: ')
b=input('Professor digite o Nome do 2ºAluno: ')
c=input('Professor digite o Nome do 3ºAluno: ')
d=input('Professor digite o Nome do 3ºAluno: ')
s=[a,b,c,d]
n=choice(s)
print ('\nProfessor o aluno escolhido foi: {:*^10}'.format(n))
