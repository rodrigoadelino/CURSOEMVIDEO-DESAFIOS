print('==================DESAFIO_075===================')
print('''Desenvolva um programa que leia quatro valores pelo teclado 
e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares..''')
print('==================PROGRAMA===================')
num =(int(input('Digite um número: ')),
      int(input('Digite outro número: ')),
      int(input('Digite mais um número: ')),
      int(input('Digite o utimo número: ')))
print ('Voce digitou os valores {}'.format(num))
#print(f'Voce digitou os valores {num}')
print('O valor 9 apareceu {} vezes'.format(num.count(9)))
#print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print('O valor 3 apareceu na {}º posicao'.format(num.index(3)+1))
else:
    print('O valor 3 não foi digitado')
#print(f'Ovalor 3 apareceu na {num.index(3)+1}ª posicao')
print('Os valores pares digitados foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end ='')