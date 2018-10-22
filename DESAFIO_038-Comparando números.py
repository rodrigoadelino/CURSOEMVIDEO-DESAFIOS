print('=====================DESAFIO_038=====================')
print('''Escreva um programa que leia dois números inteiros 
E compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais''')
print ('=====================PROGRAMA=======================')
n1=int(input('Digite o primeiro numero: '))
n2=int(input('Digite o segundo número: '))
if n1>n2:
   print('O Primeiro numero é o maior')
elif n2>n1:
   print('O segundo numero é o maior')
else:
   print ('os números sao iguais')
