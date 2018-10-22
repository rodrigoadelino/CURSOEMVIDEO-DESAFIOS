print('=====================DESAFIO_022=====================')
print('''Crie um programa que leia
o nome completo de uma pessoa e mostre:
\nO nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras ao todo sem considerar os espacos
Quantas letras tem o primeiro nome\n''')
print ('=====================PROGRAMA======================')
nome=input('Escreva seu nome completo: ')
print('Em Maisculo     :',(nome.upper())) 
print('Em Minusculo    :',(nome.lower()))
l=(nome.replace(' ',''))
print('Total de Letras :',(len(nome)))
print('Letras s/espaco :',(len(l)))   
p=(nome.split())
print('Letras no 1ºnome:',(len(p[0])))











