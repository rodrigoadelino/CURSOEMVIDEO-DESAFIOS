print('==================DESAFIO_072===================')
print('''Crie um programa que tenha uma tupla totalmente preenchida 
com uma contagem por extenso, de zero até vinte. Seu programa deverá 
ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.''')
print('==================PROGRAMA===================')
ext=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez')
num=int(input('Digite um numero entre 0 e 10: '))
while num < 0 or num >10:
    num=int(input ('Digite apenas numeros entre 0 e 10: '))
print(ext[num])