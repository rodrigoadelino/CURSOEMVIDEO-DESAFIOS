
print('=====================DESAFIO_026=====================')
print('''Faca um programa que leia
uma frase pelo teclado e mostre:
\nQuantas vezes aparece a letra "A"
\nEm que posição ela aparece pela primeira vez
\nEm qual posição ela aparece pela última vez 
\n''')
print ('=====================PROGRAMA======================')
frase=input ('Digite sua frase: ')
print('Quantidade de "A": ', (frase.lower().count('a')))
print('Primeira posicao : ',(frase.lower().find ('a')))
print('Ultima posicao   : ', (frase.lower().rfind ('a')))
print('Todas posições   : ', (len (frase)))