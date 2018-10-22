print('==================DESAFIO_074===================')
print('''Crie um programa que vai gerar cinco números 
aleatórios e colocar em uma tupla. Depois disso, mostre 
a listagem de números gerados e também indique o menor 
e o maior valor que estão na tupla.''')
print('==================PROGRAMA===================')
from random import randint
n=(randint(0,10), randint(0,10), randint (0,10),randint (0,10),randint (0,10))
print('Os valores sorteados foram:{}'.format(n,end=''))
print('O maior valor sorteado foi:{}'.format(max(n)))
print('O menor valor sorteado foi:{}'.format(min(n)))